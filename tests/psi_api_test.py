#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from pagespeed10x import psi_api
from tests import helpers

class TestPsi_api(unittest.TestCase):
    psi_results_full = helpers.load_mock_data('psi_results_full.mock')
    psi_results_no_crux = helpers.load_mock_data('psi_results_no_crux.mock')

    def test_get_meta_data(self):
        metadata_mock = helpers.load_mock_data('psi_results_full_metadata.mock')
        metadata = psi_api.get_meta_data(self.psi_results_full)

        self.assertDictEqual(metadata, metadata_mock)

    def test_get_meta_data_no_crux(self):
        metadata_mock = helpers.load_mock_data('psi_results_no_crux_metadata.mock')
        metadata = psi_api.get_meta_data(self.psi_results_no_crux)

        self.assertDictEqual(metadata, metadata_mock)

    def test_get_lab_data(self):
        labdata_mock = helpers.load_mock_data('psi_results_full_labdata.mock')
        labdata = psi_api.get_lab_data(self.psi_results_full)

        self.assertDictEqual(labdata, labdata_mock)

    def test_get_lab_data_no_crux(self):
        labdata_mock = helpers.load_mock_data('psi_results_no_crux_labdata.mock')
        labdata = psi_api.get_lab_data(self.psi_results_no_crux)

        self.assertDictEqual(labdata, labdata_mock)

    def test_get_crux_data(self):
        cruxdata_mock = helpers.load_mock_data('psi_results_full_cruxdata.mock')
        cruxdata = psi_api.get_crux_data(self.psi_results_full)

        self.assertDictEqual(cruxdata, cruxdata_mock)

    def test_get_crux_data_no_crux(self):
        cruxdata_mock = helpers.load_mock_data('psi_results_no_crux_cruxdata.mock')
        cruxdata = psi_api.get_crux_data(self.psi_results_no_crux)

        self.assertDictEqual(cruxdata, cruxdata_mock)