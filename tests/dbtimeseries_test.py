#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from pagespeed10x import dbtimeseries
from tests import helpers

class TestDbtimeseries(unittest.TestCase):
    def test_cleanup_data_full(self):
        psi_results_full_measurements = helpers.load_mock_data('psi_results_full_measurements.mock')
        cleanup_data_full_mock = helpers.load_mock_data('cleanup_data_full.mock')

        filterlist = [
            'crux_fcp_category',
            'crux_lcp_category',
            'crux_fid_category',
            'crux_cls_category',
            'lighthouse_version',
            'time'
        ]
    
        cleanup_data = dbtimeseries.cleanup_data(psi_results_full_measurements, filterlist)

        self.assertDictEqual(cleanup_data, cleanup_data_full_mock)

    def test_cleanup_data_no_crux(self):
        psi_results_no_crux_measurements = helpers.load_mock_data('psi_results_no_crux_measurements.mock')
        cleanup_data_no_crux_mock = helpers.load_mock_data('cleanup_data_no_crux.mock')

        filterlist = [
            'crux_fcp_category',
            'crux_lcp_category',
            'crux_fid_category',
            'crux_cls_category',
            'lighthouse_version',
            'time'
        ]
    
        cleanup_data = dbtimeseries.cleanup_data(psi_results_no_crux_measurements, filterlist)

        self.assertDictEqual(cleanup_data, cleanup_data_no_crux_mock)