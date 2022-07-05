#!/usr/bin/env python3
import sys
from setuptools import setup, find_packages


cfg = {
    "name": "PAN Data Processor",
    "description": "A data transforming tool for PAN",
    "author": "Abhisek Kumar Rout",
    "author_email": "abhisek.rout99@gmail.com",
    "version": "1.0",
    "scripts": ["bin/execute.py"],
    "packages": find_packages('.'),
    "install_requires": [
        "attrs==21.4.0",
        "coverage==6.4.1",
        "iniconfig==1.1.1",
        "packaging==21.3",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pyparsing==3.0.9",
        "pytest==7.1.2",
        "pytest-cov==3.0.0",
        "tomli==2.0.1",
    ]
}

setup(**cfg)
