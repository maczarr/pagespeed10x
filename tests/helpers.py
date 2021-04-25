#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import json

def load_mock_data(mock_file):
    mocks_path = Path(__file__).parent/'mocks'

    with open(mocks_path/mock_file) as json_file:
        mock_data = json.load(json_file)

    return mock_data