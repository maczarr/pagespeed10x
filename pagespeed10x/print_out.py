#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def results(metadata, labdata, cruxdata, verbose):
  if not verbose:
    return None

  print(metadata.get('time'))
  print('Lighthouse Version: {lighthouseVersion}'.format(
    lighthouseVersion = metadata.get('lighthouse_version')
  ))
  print()
  print('Score: {score:.0f} (LCP: {lcp:.1f} s; CLS: {cls:.3f}; FCP: {fcp:.1f} s; Speed Index: {speedIndex:.1f} s; TTI: {tti:.1f} s; TBT: {tbt} ms)'.format(
    score = labdata.get('score') * 100,
    lcp = labdata.get('lcp') / 1000,
    cls = labdata.get('cls') / 10,
    fcp = labdata.get('fcp') / 1000,
    speedIndex = labdata.get('speed_index') / 1000,
    tti = labdata.get('tti') / 1000,
    tbt = labdata.get('tbt')
  ))

  print()

  if (len(cruxdata) > 0):
    print('CrUX-Data')
    print('FCP: {cruxFcp:.1f} s ({cruxFcpCat}) (Good {cruxFcpGood:.0f}% / Avg {cruxFcpAvg:.0f}% / Bad {cruxFcpBad:.0f}%)'.format(
      cruxFcp = cruxdata.get('crux_fcp') / 1000,
      cruxFcpCat = cruxdata.get('crux_fcp_category'),
      cruxFcpGood = cruxdata.get('crux_fcp_proportions_good') * 100,
      cruxFcpAvg = cruxdata.get('crux_fcp_proportions_average') * 100,
      cruxFcpBad = cruxdata.get('crux_fcp_proportions_bad') * 100
    ))

    print('LCP: {cruxLcp:.1f} s ({cruxLcpCat}) (Good {cruxLcpGood:.0f}% / Avg {cruxLcpAvg:.0f}% / Bad {cruxLcpBad:.0f}%)'.format(
      cruxLcp = cruxdata.get('crux_lcp') / 1000,
      cruxLcpCat = cruxdata.get('crux_lcp_category'),
      cruxLcpGood = cruxdata.get('crux_lcp_proportions_good') * 100,
      cruxLcpAvg = cruxdata.get('crux_lcp_proportions_average') * 100,
      cruxLcpBad = cruxdata.get('crux_lcp_proportions_bad') * 100
    ))

    print('FID: {cruxFid} ms ({cruxFidCat}) (Good {cruxFidGood:.0f}% / Avg {cruxFidAvg:.0f}% / Bad {cruxFidBad:.0f}%)'.format(
      cruxFid = cruxdata.get('crux_fid'),
      cruxFidCat = cruxdata.get('crux_fid_category'),
      cruxFidGood = cruxdata.get('crux_fid_proportions_good') * 100,
      cruxFidAvg = cruxdata.get('crux_fid_proportions_average') * 100,
      cruxFidBad = cruxdata.get('crux_fid_proportions_bad') * 100
    ))

    print('CLS: {cruxCls:.3f} ({cruxClsCat}) (Good {cruxClsGood:.0f}% / Avg {cruxClsAvg:.0f}% / Bad {cruxClsBad:.0f}%)'.format(
      cruxCls = cruxdata.get('crux_cls') / 100,
      cruxClsCat = cruxdata.get('crux_cls_category'),
      cruxClsGood = cruxdata.get('crux_cls_proportions_good') * 100,
      cruxClsAvg = cruxdata.get('crux_cls_proportions_average') * 100,
      cruxClsBad = cruxdata.get('crux_cls_proportions_bad') * 100
    ))

    print()

def divider(verbose):
  if not verbose:
    return None

  print()
  _banner(40)
  print()

def _banner(length):
  border = '=' * length
  print(border)

def info(verbose, add_empty_lines, text, format=[]):
  if not verbose:
    return None

  print(text.format(*format))

  for l in range(0, add_empty_lines):
    print()