#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import getopt

def parse_args(argv):
  strategies = ['mobile','desktop']
  comment = ''
  verbose = False
  url = False

  try:
    opts, args = getopt.getopt(
      argv,
      "hs:c:u:v",
      ["help","strategy=","comment=","url=","verbose"]
    )
  except getopt.GetoptError:
    print('pagespeed10x.py -s <strategy> -c <comment> -u <url> -v')
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      print('pagespeed10x.py -s <strategy> -c <comment> -u <url> -v')
      sys.exit()
    elif opt in ("-s", "--strategy"):
      if arg in ("mobile","desktop"):
        strategies.clear()
        strategies.append(arg)
    elif opt in ("-c", "--comment"):
      comment = arg
    elif opt in ("-v", "--verbose"):
      verbose = True
    elif opt in ("-u", "--url"):
      url = []
      url.append(arg)

  return [strategies,comment,url,verbose]