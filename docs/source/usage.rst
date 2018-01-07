=====
Usage
=====

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

-------
Testing
-------

The tests included with the project can be run with:

.. code::

    $ python setup.py test

This will delegate the execution to tox.

It is possible to run just one of the test profiles, in this case the py36 profile:

.. code::

    $ python setup.py test -p "py36"