=================
Version extractor
=================

A tool for extracting the version of a Python file.

.. image:: https://badge.fury.io/py/bernardomg.version-extractor.svg
    :target: https://pypi.python.org/pypi/bernardomg.version-extractor
    :alt: Version extractor Pypi package page

.. image:: https://img.shields.io/badge/docs-release-blue.svg
    :target: http://docs.bernardomg.com/python-version-extractor
    :alt: Version extractor latest documentation Status
.. image:: https://img.shields.io/badge/docs-develop-blue.svg
    :target: http://docs.bernardomg.com/development/python-version-extractor
    :alt: Version extractor development documentation Status

Features
--------

- Extract the value from a version field inside any Python file

Documentation
-------------

Documentation sources are included with the project, and used to generate the
documentation sites:

- The `latest docs`_ are always generated for the latest release, kept in the 'master' branch
- The `development docs`_ are generated from the latest code in the 'develop' branch

You can also create the documentation from the source files, kept in the 'docs'
folder, with the help of `Sphinx`_. For this use the makefile, or the make.bat
file, contained on that folder.

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 3.4
- Python 3.5
- Python 3.6
- Pypy 3

All other dependencies are indicated on the requirements.txt file.

These can be installed with:

``$ pip install --upgrade -r requirements.txt``

Installing
~~~~~~~~~~

The project is offered as a `Pypi package`_, and using pip is the preferred way
to install it. For this use the following command;

``$ pip install bernardomg.version-extractor``

If needed, manual installation is possible:

``$ python setup.py install``

Usage
-----

Just import and use the function::

    from version_extractor import extract_version

    version = extract_version('tests/resources/__init__.py')

Or use a preconfigured function::

    from version_extractor import extract_version_init

    version = extract_version_init('tests/resources')

This is useful when setting up a setup.py file::

    setup(
        ...
        version=extract_version_init(_source_package),
        ...
    )

Testing
-------

The tests included with the project can be run with:

``$ python setup.py test``

This will delegate the execution to tox.

It is possible to run just one of the test profiles, in this case the py36 profile:

``$ python setup.py test -p "py36"``

Collaborate
-----------

Any kind of help with the project will be well received, and there are two main ways to give such help:

- Reporting errors and asking for extensions through the issues management
- or forking the repository and extending the project

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues tracker`_, where any Github
user may report bugs or ask for new features.

Getting the code
~~~~~~~~~~~~~~~~

If you wish to fork or modify the code, visit the `GitHub project page`_, where
the latest versions are always kept. Check the 'master' branch for the latest
release, and the 'develop' for the current, and stable, development version.

License
-------

The project has been released under the `MIT License`_.

.. _GitHub project page: https://github.com/Bernardo-MG/python-version-extractor
.. _latest docs: http://docs.bernardomg.com/python-version-extractor
.. _development docs: http://docs.bernardomg.com/development/python-version-extractor
.. _Pypi package: https://pypi.python.org/pypi/bernardomg.version-extractor
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
.. _project issues tracker: https://github.com/Bernardo-MG/python-version-extractor/issues
.. _Sphinx: http://sphinx-doc.org/
