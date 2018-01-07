# -*- coding: utf-8 -*-

import unittest

from bernardomg.version_extractor import extract_version

"""
Placeholder tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestExtractVersion(unittest.TestCase):
    """
    Placeholder for a test case.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        pass

    def test_sample_file(self):
        """
        Reads the sample file and returns its version.

        This is the simples use case.
        """
        version = extract_version('../testresources/__init__.py')
        self.assertEqual('1.2.3', version)

    def test_empty_file(self):
        """
        Reads an empty file and tries to return its version.

        This is the simples use case.
        """
        version = extract_version('../testresources/empty.py')
        self.assertFalse(version)