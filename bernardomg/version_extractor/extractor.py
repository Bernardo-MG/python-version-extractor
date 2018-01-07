# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

"""
Placeholder classes.

Replace this module for the actual code.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


def extract_version(path):
    """
    Reads the file at the specified path and returns the version contained in it.

    This is meant for reading the __init__.py file inside a package, and so it
    expects a version field like:

    __version__ = '1.0.0'

    :param path: path to the Python file
    :return: the version inside the file
    """

    # Regular expression for the version
    _version_re = re.compile(r'__version__\s+=\s+(.*)')

    with open(path + '__init__.py', 'rb', encoding='utf-8') as f:
        version_lib = f.read()

    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))

    return version_lib
