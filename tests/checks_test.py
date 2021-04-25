#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import io
import sys
from collections import namedtuple
from pagespeed10x import checks

class TestChecks(unittest.TestCase):
    def test_incorrect_python_version(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        test_output = '''This script requires Python 3.9!
You are using Python 3.7.
'''

        mock_sys_version = namedtuple('mock_sys_version', 'major minor')
        mock_sys_version.major = 3
        mock_sys_version.minor = 7

        with self.assertRaises(SystemExit) as cm:
            checks.python_version(mock_sys_version)

        self.assertEqual(capturedOutput.getvalue(), test_output)
        self.assertEqual(cm.exception.code, 1)

        sys.stdout = sys.__stdout__

    def test_correct_python_version(self):
        mock_sys_version = namedtuple('mock_sys_version', 'major minor')
        mock_sys_version.major = 3
        mock_sys_version.minor = 9

        self.assertIsNone(checks.python_version(mock_sys_version))

    def test_valid_key(self):
        input_int = checks._valid_key(5)
        input_incorrect_str = checks._valid_key('')
        input_str = checks._valid_key('foobar')

        self.assertFalse(input_int)
        self.assertFalse(input_incorrect_str)
        self.assertTrue(input_str)

    def test_valid_urls(self):
        input_int = checks._valid_urls(5)
        input_str = checks._valid_urls('foobar')
        input_incorrect_list = checks._valid_urls([])
        input_list = checks._valid_urls(['https://www.webpage.testtld'])

        self.assertFalse(input_int)
        self.assertFalse(input_str)
        self.assertFalse(input_incorrect_list)
        self.assertTrue(input_list)

    def test_incorrect_apikey_and_urls(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        test_output = '''You need to set an API_KEY env-variable and at least one URL in the TESTSITES env-variable.
e.g. in an .env file:

PAGESPEED_INSIGHTS_API_KEY=<your api key>
TESTSITES='[
  "https://www.example.com",
  "https://www.example2.com"
]'
'''

        with self.assertRaises(SystemExit) as cm:
            checks.apikey_and_urls(5, ['https://www.webpage.testtld'])
            
        self.assertEqual(capturedOutput.getvalue(), test_output)
        self.assertEqual(cm.exception.code, 1)

        sys.stdout = sys.__stdout__

    def test_correct_apikey_and_urls(self):
        input_correct = checks.apikey_and_urls('barbaz',['https://domain.tld'])

        self.assertIsNone(input_correct)

    def test_valid_id(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        test_output = '''Error: The given id (HOST_UID) must be an integer.
e.g. in an .env file:

HOST_UID=1000

invalid literal for int() with base 10: 'foobar'
'''

        input_none_id = checks.valid_id(None, 'foo')
        input_int_str = checks.valid_id('1000', 'HOST_UID')

        self.assertFalse(input_none_id)
        self.assertEquals(input_int_str, 1000)

        with self.assertRaises(SystemExit) as cm:
            checks.valid_id('foobar', 'HOST_UID')
            
        self.assertEqual(capturedOutput.getvalue(), test_output)
        self.assertEqual(cm.exception.code, 1)

        sys.stdout = sys.__stdout__