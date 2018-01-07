===============================
Version extractor
===============================

This is a project created with the `Cookiecutter Python Library
<https://github.com/Bernardo-MG/cookiecutter-python-library>`_ template and
ready to be used for creating a new Python library.

Just check the readme and docs, to adapt them to your project, and it is done.

Remember that if you want to create a new project it is better just reusing
the Cookiecutter Python Library template, as this will set up the initial
project according to a few pieces of data it will ask for.

.. image:: https://badge.fury.io/py/bernardomg.version-extractor.svg
    :target: https://pypi.python.org/pypi/bernardomg.version-extractor
    :alt: Version extractor Pypi package page

.. image:: https://img.shields.io/badge/docs-release-blue.svg
    :target: http://docs.bernardomg.com/bernardomg.version-extractor
    :alt: Version extractor latest documentation Status
.. image:: https://img.shields.io/badge/docs-develop-blue.svg
    :target: http://docs.bernardomg.com/development/bernardomg.version-extractor
    :alt: Version extractor development documentation Status

Features
--------

- Travis configuration file
- Customized setup.py module to minimize configuration, and using tox for the tests
- Docs using `Sphinx`_ and the `Sphinx Docs Theme <https://github.com/Bernardo-MG/sphinx-docs-theme>`_
- Prepared to run tests through tox
- Prepared to run tests on Python 2 and 3
- Prepared to run tests on pypy and pypy 3
- Prepared to run coverage tests and integrate with `Coveralls <https://coveralls.io>`_
- Prepared to run tests for the `Sphinx`_ documentation

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

- Python 2.7
- Python 3.4
- Python 3.5
- Python 3.6
- Pypy
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

The application has been coded in Python, and does not require any particular
framework.

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
.. _latest docs: http://docs.bernardomg.com/bernardomg.version-extractor
.. _development docs: http://docs.bernardomg.com/development/bernardomg.version-extractor
.. _Pypi package: https://pypi.python.org/pypi/bernardomg.version-extractor
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
.. _project issues tracker: https://github.com/Bernardo-MG/python-version-extractor/issues
.. _Sphinx: http://sphinx-doc.org/
