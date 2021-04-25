#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def python_version(version):
  if not (version.major == 3 and version.minor >= 9):
    print('This script requires Python 3.9!')
    print('You are using Python {major}.{minor}.'.format(
      major = version.major,
      minor = version.minor
    ))
    sys.exit(1)

def _valid_key(key):
  return (isinstance(key, str) and len(key) > 0)

def _valid_urls(urls):
  return (isinstance(urls, list) and len(urls) > 0)

def apikey_and_urls(key, urls):
  if (not _valid_key(key) or not _valid_urls(urls)):
    print('You need to set an API_KEY env-variable and at least one URL in the TESTSITES env-variable.')
    print('e.g. in an .env file:')
    print()
    print('PAGESPEED_INSIGHTS_API_KEY=<your api key>')
    print('TESTSITES=\'[')
    print('  "https://www.example.com",')
    print('  "https://www.example2.com"')
    print(']\'')
    sys.exit(1)

def valid_id(id, name):
  if id == None:
    return False

  try:
    return int(id)
  except ValueError as err:
    print('Error: The given id ({}) must be an integer.'.format(name))
    print('e.g. in an .env file:')
    print()
    print('{}=1000'.format(name))
    print()
    print(err)
    sys.exit(1)