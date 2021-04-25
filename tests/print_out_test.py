#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io
import unittest
from pagespeed10x import print_out
from tests import helpers

class TestPrint_out(unittest.TestCase):
    psi_results_full = helpers.load_mock_data('psi_results_full.mock')
    psi_results_no_crux = helpers.load_mock_data('psi_results_no_crux.mock')

    def test_results_full(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        metadata_mock = helpers.load_mock_data('psi_results_full_metadata.mock')
        labdata_mock = helpers.load_mock_data('psi_results_full_labdata.mock')
        cruxdata_mock = helpers.load_mock_data('psi_results_full_cruxdata.mock')

        verbose = True

        print_out.results(metadata_mock, labdata_mock, cruxdata_mock, verbose)

        results_output = '''2021-04-24T15:31:03.860Z
Lighthouse Version: 7.3.0

Score: 73 (LCP: 2.0 s; CLS: 0.000; FCP: 1.1 s; Speed Index: 1.9 s; TTI: 2.3 s; TBT: 294 ms)

CrUX-Data
FCP: 1.4 s (AVERAGE) (Good 52% / Avg 44% / Bad 3%)
LCP: 2.0 s (FAST) (Good 84% / Avg 10% / Bad 6%)
FID: 4 ms (FAST) (Good 99% / Avg 1% / Bad 0%)
CLS: 0.190 (AVERAGE) (Good 59% / Avg 24% / Bad 17%)

'''

        self.assertEqual(capturedOutput.getvalue(), results_output)

        sys.stdout = sys.__stdout__

    def test_results_no_crux(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        metadata_mock = helpers.load_mock_data('psi_results_no_crux_metadata.mock')
        labdata_mock = helpers.load_mock_data('psi_results_no_crux_labdata.mock')
        cruxdata_mock = helpers.load_mock_data('psi_results_no_crux_cruxdata.mock')

        verbose = True

        print_out.results(metadata_mock, labdata_mock, cruxdata_mock, verbose)

        results_output = '''2021-04-24T15:36:18.287Z
Lighthouse Version: 7.3.0

Score: 100 (LCP: 0.3 s; CLS: 0.003; FCP: 0.2 s; Speed Index: 0.3 s; TTI: 0.2 s; TBT: 0 ms)

'''

        self.assertEqual(capturedOutput.getvalue(), results_output)

        sys.stdout = sys.__stdout__

    def test_results_not_verbose(self):
        verbose = False

        results = print_out.results({}, {}, {}, verbose)

        self.assertIsNone(results)

    def test_divider(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        verbose = True

        print_out.divider(verbose)

        results_output = '''
========================================

'''

        self.assertEqual(capturedOutput.getvalue(), results_output)

        sys.stdout = sys.__stdout__

    def test_divider_not_verbose(self):
        verbose = False

        results = print_out.divider(verbose)

        self.assertIsNone(results)

    def test_banner(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        print_out._banner(0)

        results_output = '''
'''

        self.assertEqual(capturedOutput.getvalue(), results_output)

        capturedOutput.truncate(0)
        capturedOutput.seek(0)

        print_out._banner(12)

        results_output_banner = '''============
'''

        self.assertEqual(capturedOutput.getvalue(), results_output_banner)

        sys.stdout = sys.__stdout__

    def test_info(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        verbose = True

        print_out.info(verbose, 2, 'This is a Test.')

        results_output = '''This is a Test.


'''

        self.assertEqual(capturedOutput.getvalue(), results_output)

        sys.stdout = sys.__stdout__

    def test_info_with_format(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        verbose = True

        print_out.info(verbose, 4, 'This {} {} {}.', ['is','a','Test'])

        results_output = '''This is a Test.




'''

        self.assertEqual(capturedOutput.getvalue(), results_output)

        sys.stdout = sys.__stdout__

    def test_info_not_verbose(self):
        verbose = False

        results = print_out.info(verbose, 200, 'Foo Bar {}', ['Baz'])

        self.assertIsNone(results)