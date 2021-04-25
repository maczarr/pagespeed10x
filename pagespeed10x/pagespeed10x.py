#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import checks
import sys

checks.python_version(sys.version_info)

import os
import json
from dotenv import load_dotenv
from pathlib import Path
import parse_cli_args
import dbsql
import psi_api
import dbtimeseries
import print_out

root_path = Path(__file__).parent.parent
dotenv_path = root_path/'.env'
load_dotenv(dotenv_path)

API_KEY = os.getenv('PAGESPEED_INSIGHTS_API_KEY')
API_ENDPOINT = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={website}&key={apikey}&strategy={strategy}'
TESTSITES = json.loads(os.getenv('TESTSITES', '[]'))

DB_SQL_ON = os.getenv('DB_SQL_ON', 'False').lower() in ['true', '1']
DB_SQL_PATH = root_path/'storage'/'sqlite'
DB_SQL_FILE = os.getenv('DB_SQL_FILENAME', 'pagespeed10x.sqlite.db')
DB_SQL_TABLE = os.getenv('DB_SQL_TABLE', 'measurements')

INFLUXDB_ON = os.getenv('INFLUXDB_ON', 'False').lower() in ['true', '1']
INFLUXDB_TOKEN = os.getenv('INFLUXDB_TOKEN')
INFLUXDB_ORG = os.getenv('INFLUXDB_ORG')
INFLUXDB_BUCKET = os.getenv('INFLUXDB_BUCKET')
INFLUXDB_HOST = os.getenv('INFLUXDB_HOST')
INFLUXDB_PORT = os.getenv('INFLUXDB_PORT', 8086)
INFLUXDB_HOST_AND_PORT = '{host}:{port}'.format(
  host = INFLUXDB_HOST,
  port = INFLUXDB_PORT
)

HOST_UID = checks.valid_id(os.getenv('HOST_UID'), 'HOST_UID')
HOST_GID = checks.valid_id(os.getenv('HOST_GID'), 'HOST_GID')

VERBOSE = os.getenv('VERBOSE', 'False').lower() in ['true', '1']

def _performance_test(testpage, strategy, comment, api_key, api_endpoint, verbose):
  results = psi_api.get_test_results(testpage, strategy, api_key, api_endpoint)
  
  metadata = psi_api.get_meta_data(results)
  labdata = psi_api.get_lab_data(results)
  cruxdata = psi_api.get_crux_data(results)

  measurements = metadata | labdata

  if (len(cruxdata) > 0):
    measurements = measurements | cruxdata

  print_out.results(metadata, labdata, cruxdata, verbose)

  if (DB_SQL_ON):
    if (dbsql.db_exists_or_init(DB_SQL_PATH, DB_SQL_FILE, DB_SQL_TABLE, verbose, HOST_UID, HOST_GID)):
      conn = dbsql.connect_db(DB_SQL_PATH, DB_SQL_FILE)

      dbsql.save_data(conn, DB_SQL_TABLE, testpage, strategy, measurements, comment, verbose)
      dbsql.disconnect_db(conn)

  if (INFLUXDB_ON):
    filterlist = [
      'crux_fcp_category',
      'crux_lcp_category',
      'crux_fid_category',
      'crux_cls_category',
      'lighthouse_version',
      'time'
    ]
    measurements['filtered'] = dbtimeseries.cleanup_data(measurements, filterlist)

    tsdbclient, tsdbwriteclient = dbtimeseries.connect_db(INFLUXDB_HOST_AND_PORT, INFLUXDB_TOKEN, INFLUXDB_ORG)

    try:
      dbtimeseries.save_data(tsdbwriteclient, INFLUXDB_BUCKET, INFLUXDB_ORG, testpage, strategy, measurements, verbose)
    except Exception:
      sys.exit(1)
    finally:
      dbtimeseries.disconnect_db(tsdbwriteclient, tsdbclient)

def main(argv):
  strategies, comment, url, verbose = parse_cli_args.parse_args(argv)
  verbose = verbose or VERBOSE
  urls = url or TESTSITES

  checks.apikey_and_urls(API_KEY, urls)

  for url in urls:
    for strategy in strategies:
      print_out.info(verbose, 1, '{} ({})', [url, strategy])

      _performance_test(url, strategy, comment, API_KEY, API_ENDPOINT, verbose)

      print_out.divider(verbose)

if __name__ == "__main__":
  main(sys.argv[1:])
