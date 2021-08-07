#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='pagespeed10x',
    version='1.2.0',
    description='Get regular PageSpeed Insights results and store or visualize them.',
    author='Hilko Holweg',
    author_email='hilko@holweg.name',
    url='https://github.com/maczarr/pagespeed10x',
    python_requires='>=3.9',
    packages=[
        'pagespeed10x'
    ],
    entry_points={
        'console_scripts': ['pagespeed10x=pagespeed10x.pagespeed10x:main'],
    },
    install_requires=[
        'requests==2.25.1',
        'python-dotenv==0.17.0',
        'influxdb-client==1.16.0',
        'nose2==0.10.0'
    ],
)