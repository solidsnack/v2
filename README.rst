======
``v2``
======

.. image:: https://travis-ci.org/solidsnack/v2.svg?branch=master
    :target: https://travis-ci.org/solidsnack/v2
.. image:: https://img.shields.io/pypi/v/v2.svg
    :target: https://pypi.python.org/pypi/v2
.. image:: https://img.shields.io/pypi/dd/v2.svg
    :target: https://pypi.python.org/pypi/v2

``v2`` provides for auto-versioning in an intuitive way.

From ``setup.py``:

.. code:: python

    from v2 import v2

    setup(
          # ...
          version=v2.from_git().from_file().imprint().version,
          # ...
          setup_requires=[..., 'v2', ...],
    )

From within your package root:

.. code:: python

    from v2 import v2

    __version__ = v2.from_pkg().from_git().from_default().version

