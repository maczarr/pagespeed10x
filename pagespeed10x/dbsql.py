#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
import print_out

def connect_db(db_path, db_file):
  connection = None

  try:
    os.makedirs(db_path, exist_ok=True)
    connection = sqlite3.connect(db_path / db_file)
  except IOError as err:
    print('Error: Could not connect to SQLite3 database.')
    print(err)
  except Exception as e:
    print(e)
  finally:
    return connection

def _init_db(db_path, db_file, db_table, host_uid, host_gid):
  conn = connect_db(db_path, db_file)

  if (conn == None):
    return False

  cursor = conn.cursor()
  sql_query = 'CREATE TABLE {table} (id INTEGER PRIMARY KEY,\
    url STRING NOT NULL, strategy STRING NOT NULL, comment STRING NOT NULL,\
    time STRING NOT NULL, lighthouse_version STRING NOT NULL,\
    score FLOAT NOT NULL, fcp FLOAT NOT NULL, speed_index FLOAT NOT NULL,\
    lcp FLOAT NOT NULL, tti FLOAT NOT NULL, tbt FLOAT NOT NULL,\
    cls FLOAT NOT NULL, crux_fcp FLOAT, crux_fcp_category STRING,\
    crux_fcp_proportions_good FLOAT, crux_fcp_proportions_average FLOAT,\
    crux_fcp_proportions_bad FLOAT, crux_lcp FLOAT, crux_lcp_category STRING,\
    crux_lcp_proportions_good FLOAT, crux_lcp_proportions_average FLOAT,\
    crux_lcp_proportions_bad FLOAT, crux_fid INTEGER, crux_fid_category STRING,\
    crux_fid_proportions_good FLOAT, crux_fid_proportions_average FLOAT,\
    crux_fid_proportions_bad FLOAT, crux_cls FLOAT, crux_cls_category STRING,\
    crux_cls_proportions_good FLOAT, crux_cls_proportions_average FLOAT,\
    crux_cls_proportions_bad FLOAT)'.format(
      table = db_table
    )

  try:
    cursor.execute(sql_query)
    conn.commit()
    disconnect_db(conn)

    if (host_uid and host_gid):
      os.chmod(db_path/db_file, 0o664)
      os.chown(db_path/db_file, host_uid, host_gid)

    return True
  except sqlite3.DatabaseError as db_err:
    print('Error: Could not initialize SQLite3 database.')
    print(db_err)
    return False
  except sqlite3.Error as e:
    print('Error: There was an error while initializing the SQLite3 database.')
    print(e)
    return False

def db_exists_or_init(db_path, db_file, db_table, verbose, host_uid, host_gid):
  if not os.path.exists(db_path / db_file):
    create_db = _init_db(db_path, db_file, db_table, host_uid, host_gid)

    if create_db:
      print_out.info(verbose, 1, 'Database {} has been successfully created.', [db_file])
      return True
    else:
      return False
  else:
    return True

def save_data(conn, db_table, testpage, strategy, measurements, comment, verbose):
  if (conn == None):
    return False

  try:
    cursor = conn.cursor()
    db_cols = ['id', 'url', 'strategy', 'comment', *measurements.keys()]
    sql_query = 'INSERT INTO {table} ({cols}) VALUES({cols_vals})'.format(
      table = db_table,
      cols = ','.join(db_cols),
      cols_vals = ','.join('?' for _ in range(len(db_cols)))
    )
    sql_values = (None, testpage, strategy, comment, *measurements.values())

    cursor.execute(sql_query, sql_values)
    conn.commit()

    print_out.info(verbose, 0, 'Measurements have been saved to the SQLite3 database.')
  except sqlite3.OperationalError as err:
    print('Error: Measurements have not been saved to SQLite3 database.')
    print(err)
  except sqlite3.Error as e:
    print(e)

def disconnect_db(conn):
  if (conn == None):
    return False

  try:
    conn.close()
    return True
  except IOError as err:
    print('Error: Could not reach SQLite3 database to close connection.')
    print(err)
    return False
  except Exception as e:
    print(e)
    return False