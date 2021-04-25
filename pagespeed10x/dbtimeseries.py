#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import urllib3
import print_out
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

def connect_db(url, token, org):
  try:
    _client = InfluxDBClient(url=url, token=token, debug=False, org=org)
    _write_client = _client.write_api(write_options=SYNCHRONOUS)

    return [_client, _write_client]
  except Exception as e:
    print('Error: An Error occured while connecting to InfluxDB.')
    print(e)
    sys.exit(1)

def save_data(write_client, bucket, org, testpage, strategy, measurements, verbose):
  try:
    dataset = {
      "measurement": "lighthouse_performance_data",
      "tags": {
        "url": testpage,
        "lighthouse_version": measurements.get('lighthouse_version'),
        "strategy": strategy
      },
      "fields": measurements['filtered'],
      "time": measurements.get('time')
    }

    write_client.write(bucket=bucket, org=org, record=dataset)

    print_out.info(verbose, 1, 'Measurements have been saved to  InfluxDB.')
  except urllib3.exceptions.NewConnectionError as conn_err:
    print('Error: Could not reach InfluxDB while trying to write data.')
    print(conn_err)
    sys.exit(1)
  except Exception as e:
    print('Error: An error occured while writing data to InfluxDB.')
    print(e)
    raise

def disconnect_db(write_client, client):
  try:
    write_client.close()
    client.close()
    return True
  except Exception as e:
    print('Error: Could not reach InfluxDB to close connection.')
    print(e)
    return False

def cleanup_data(dict, keys_to_filter_out):
  return { key:float(val) for key, val in dict.items() if key not in keys_to_filter_out}