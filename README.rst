.. image:: https://travis-ci.org/lukassup/crud-cli.svg?branch=master
    :target: https://travis-ci.org/lukassup/crud-cli

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

    $ git clone https://github.com/lukassup/crud-cli.git
    $ pip install ./crud-cli

For instructions on installing python and pip see "The Hitchhiker's Guide to
Python" `Installation Guides
<http://docs.python-guide.org/en/latest/starting/installation/>`_.

Alternatively use ``easy_install``:

.. code-block:: bash

    $ git clone https://github.com/lukassup/crud-cli.git
    $ easy_install ./crud-cli

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

    $ crud-cli --help
    usage: crud-cli [-h] {create} ...

    positional arguments:
    {create}    subcommands

    optional arguments:
    -h, --help  show this help message and exit


.. _development:

Development
-----------

Install the ``crud-cli`` package in editable mode using ``pip``:

.. code-block:: bash

    $ git clone https://github.com/lukassup/crud-cli.git
    $ pip install -e ./crud-cli

.. _testing:

Testing
-------

Run the tests:

.. code-block:: bash

    $ git clone https://github.com/lukassup/crud-cli.git
    $ cd route-cli
    $ python2 setup.py test
    $ python3 setup.py test
