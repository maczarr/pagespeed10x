#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys

def get_test_results(testpage, strategy, api_key, api_endpoint):
  try:
    response = requests.get(url=api_endpoint.format(
      website = testpage,
      apikey = api_key,
      strategy = strategy
    ))
    response.raise_for_status()
  except requests.exceptions.Timeout:
    print('Error: The request timed out, please try again.')
    sys.exit(1)
  except requests.exceptions.HTTPError as err:
    print('Error: A HTTP-Error occured.')
    print(err)
    sys.exit(1)
  except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

  return response.json()

def get_lab_data(testResult):
  labResults = testResult['lighthouseResult']['audits']

  return {
    "score" : _get_score(testResult),
    "fcp" : _get_fcp(labResults),
    "speed_index" : _get_speed_index(labResults),
    "lcp" : _get_lcp(labResults),
    "tti" : _get_tti(labResults),
    "tbt" : _get_tbt(labResults),
    "cls" : _get_cls(labResults)
  }

def get_meta_data(testResult):
  return {
    "time" : _get_timestamp(testResult),
    "lighthouse_version" : _get_lighthouse_version(testResult)
  }

def get_crux_data(testResult):
  crux_section = testResult['loadingExperience']

  if (not 'metrics' in crux_section or 'origin_fallback' in crux_section):
    return {}

  cruxResults = crux_section['metrics']

  return {
    "crux_fcp" : _get_crux_fcp(cruxResults),
    "crux_fcp_category" : _get_crux_fcp_category(cruxResults),
    "crux_fcp_proportions_good" : _get_crux_fcp_proportions_good(cruxResults),
    "crux_fcp_proportions_average" : _get_crux_fcp_proportions_average(cruxResults),
    "crux_fcp_proportions_bad" : _get_crux_fcp_proportions_bad(cruxResults),
    "crux_lcp" : _get_crux_lcp(cruxResults),
    "crux_lcp_category" : _get_crux_lcp_category(cruxResults),
    "crux_lcp_proportions_good" : _get_crux_lcp_proportions_good(cruxResults),
    "crux_lcp_proportions_average" : _get_crux_lcp_proportions_average(cruxResults),
    "crux_lcp_proportions_bad" : _get_crux_lcp_proportions_bad(cruxResults),
    "crux_fid" : _get_crux_fid(cruxResults),
    "crux_fid_category" : _get_crux_fid_category(cruxResults),
    "crux_fid_proportions_good" : _get_crux_fid_proportions_good(cruxResults),
    "crux_fid_proportions_average" : _get_crux_fid_proportions_average(cruxResults),
    "crux_fid_proportions_bad" : _get_crux_fid_proportions_bad(cruxResults),
    "crux_cls" : _get_crux_cls(cruxResults),
    "crux_cls_category" : _get_crux_cls_category(cruxResults),
    "crux_cls_proportions_good" : _get_crux_cls_proportions_good(cruxResults),
    "crux_cls_proportions_average" : _get_crux_cls_proportions_average(cruxResults),
    "crux_cls_proportions_bad" : _get_crux_cls_proportions_bad(cruxResults)
  }

def _get_timestamp(testResult):
  return testResult['analysisUTCTimestamp']

def _get_lighthouse_version(testResult):
  return testResult['lighthouseResult']['lighthouseVersion']

# Lab-Data
def _get_score(testResult):
  return testResult['lighthouseResult']['categories']['performance']['score']

def _get_fcp(testResult):
  return testResult['first-contentful-paint']['numericValue']

def _get_speed_index(testResult):
  return testResult['speed-index']['numericValue']

def _get_lcp(testResult):
  return testResult['largest-contentful-paint']['numericValue']

def _get_tti(testResult):
  return testResult['interactive']['numericValue']

def _get_tbt(testResult):
  return testResult['total-blocking-time']['numericValue']

def _get_cls(testResult):
  return testResult['cumulative-layout-shift']['numericValue']

# Field-/CrUX-Data
def _get_crux_fcp(testResult):
  return testResult['FIRST_CONTENTFUL_PAINT_MS']['percentile']

def _get_crux_fcp_category(testResult):
  return testResult['FIRST_CONTENTFUL_PAINT_MS']['category']

def _get_crux_fcp_proportions_good(testResult):
  return testResult['FIRST_CONTENTFUL_PAINT_MS']['distributions'][0]['proportion']

def _get_crux_fcp_proportions_average(testResult):
  return testResult['FIRST_CONTENTFUL_PAINT_MS']['distributions'][1]['proportion']

def _get_crux_fcp_proportions_bad(testResult):
  return testResult['FIRST_CONTENTFUL_PAINT_MS']['distributions'][2]['proportion']

def _get_crux_lcp(testResult):
  return testResult['LARGEST_CONTENTFUL_PAINT_MS']['percentile']

def _get_crux_lcp_category(testResult):
  return testResult['LARGEST_CONTENTFUL_PAINT_MS']['category']

def _get_crux_lcp_proportions_good(testResult):
  return testResult['LARGEST_CONTENTFUL_PAINT_MS']['distributions'][0]['proportion']

def _get_crux_lcp_proportions_average(testResult):
  return testResult['LARGEST_CONTENTFUL_PAINT_MS']['distributions'][1]['proportion']

def _get_crux_lcp_proportions_bad(testResult):
  return testResult['LARGEST_CONTENTFUL_PAINT_MS']['distributions'][2]['proportion']

def _get_crux_fid(testResult):
  return testResult['FIRST_INPUT_DELAY_MS']['percentile']

def _get_crux_fid_category(testResult):
  return testResult['FIRST_INPUT_DELAY_MS']['category']

def _get_crux_fid_proportions_good(testResult):
  return testResult['FIRST_INPUT_DELAY_MS']['distributions'][0]['proportion']

def _get_crux_fid_proportions_average(testResult):
  return testResult['FIRST_INPUT_DELAY_MS']['distributions'][1]['proportion']

def _get_crux_fid_proportions_bad(testResult):
  return testResult['FIRST_INPUT_DELAY_MS']['distributions'][2]['proportion']

def _get_crux_cls(testResult):
  return testResult['CUMULATIVE_LAYOUT_SHIFT_SCORE']['percentile']

def _get_crux_cls_category(testResult):
  return testResult['CUMULATIVE_LAYOUT_SHIFT_SCORE']['category']

def _get_crux_cls_proportions_good(testResult):
  return testResult['CUMULATIVE_LAYOUT_SHIFT_SCORE']['distributions'][0]['proportion']

def _get_crux_cls_proportions_average(testResult):
  return testResult['CUMULATIVE_LAYOUT_SHIFT_SCORE']['distributions'][1]['proportion']

def _get_crux_cls_proportions_bad(testResult):
  return testResult['CUMULATIVE_LAYOUT_SHIFT_SCORE']['distributions'][2]['proportion']