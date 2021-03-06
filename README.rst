.. image:: https://travis-ci.org/lukassup/python-cli.svg?branch=master
    :target: https://travis-ci.org/lukassup/python-cli

crud-cli
========

``crud-cli`` is a simple Python CLI CRUD application skeleton

.. _installation:

Installation
------------

Supported versions of Python are: 2.6, 2.7, 3.4, 3.5 and 3.6. The
recommended way to install this package is via `pip
<https://pypi.python.org/pypi/pip>`_.

.. code-block:: bash

    $ git clone https://github.com/lukassup/python-cli.git
    $ pip install ./python-cli

For instructions on installing python and pip see "The Hitchhiker's Guide to
Python" `Installation Guides
<http://docs.python-guide.org/en/latest/starting/installation/>`_.

Alternatively use ``easy_install``:

.. code-block:: bash

    $ git clone https://github.com/lukassup/python-cli.git
    $ easy_install ./python-cli

.. _usage:

Usage
-----

Create CLI scripts quickly using function decorators

.. code-block:: python

    from crud_cli import CLI

    cli = CLI()

    @cli.command('create')
    @cli.option('name')
    @cli.option('-s', '--size', type=int, choices=range(3))
    def create_command(name, size):
        """Creates a resource."""
        print('creating resource')
        print('name: %r' % name)
        print('size: %r' % size)

    cli.run()


Script help and argument parsing is performed by argparse library behind the
curtains

.. code-block::

    $ crud-cli create --help
    usage: crud-cli create [-h] [-v | -q] [-s {0,1,2}] name

    Creates a resource.

    positional arguments:
    name

    optional arguments:
    -h, --help            show this help message and exit
    -v, --verbose         more verbose
    -q, --quiet           less verbose
    -s {0,1,2}, --size {0,1,2}


.. _development:

Development
-----------

Install the ``python-cli`` package in editable mode using ``pip``:

.. code-block:: bash

    $ git clone https://github.com/lukassup/python-cli.git
    $ pip install -e ./python-cli

.. _testing:

Testing
-------

Run the tests:

.. code-block:: bash

    $ git clone https://github.com/lukassup/python-cli.git
    $ cd python-cli
    $ python2 setup.py test
    $ python3 setup.py test
