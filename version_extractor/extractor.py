# -*- coding: utf-8 -*-

import ast
import re

"""
Placeholder classes.

Replace this module for the actual code.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

def extract_version(path):
    """
    Reads the file at the specified path and returns the version contained in it.

    This is meant for reading the __init__.py file inside a package, and so it
    expects a version field like:

    __version__ = '1.0.0'

    :param path: path to the Python file
    :return: the version inside the file
    """

    with open(path, 'r', encoding='utf-8') as f:
        version = f.read()

    if version:
        version = _version_re.search(version)
        if version:
            version = version.group(1)
            version = str(ast.literal_eval(version.rstrip()))
            extracted = version
        else:
            extracted = None
    else:
        extracted = None

    return extracted


def extract_version_init(folder):
    """
    Reads the __init__.py file inside the specified folder and returns the version
    contained in it.

    This is meant for reading the __init__.py file inside a package, and so it
    expects a version field like:

    __version__ = '1.0.0'

    :param folder: folder containing the __init__.py file
    :return: the version inside the file
    """

    return extract_version(folder + '__init__.py')
