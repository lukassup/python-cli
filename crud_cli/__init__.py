#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""An example CRUD CLI app."""

from __future__ import (
    absolute_import,
    print_function,
    unicode_literals
)

import argparse
import json
import logging
import sys


TAGS = (
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'black',
    'white',
    'gray',
)


class CLI(object):

    """A really basic version of the famous Python Click library."""

    log = logging.getLogger(__name__)
    common_args = argparse.ArgumentParser(add_help=False)
    log_group = common_args.add_mutually_exclusive_group()
    log_group.add_argument(
        '-v',
        '--verbose',
        dest='verbosity',
        default=[logging.INFO],
        action='append_const',
        const=-10,
        help='more verbose',
    )
    log_group.add_argument(
        '-q',
        '--quiet',
        dest='verbosity',
        action='append_const',
        const=10,
        help='less verbose',
    )

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='subcommands',
                                                     dest='command')
        self.subparsers.required = True

    def command(self, name, *args, **kwargs):
        """Register a function to the command-line interface."""
        def wrapper(f):
            f.parser = self.subparsers.add_parser(
                    name, *args, description=f.__doc__,
                    parents=[self.common_args], **kwargs)
            if getattr(f, 'cli_args', None) is not None:
                for fargs, fkwargs in f.cli_args:
                    f.parser.add_argument(*fargs, **fkwargs)
            f.parser.set_defaults(action=f)
            return f
        return wrapper

    def option(self, *args, **kwargs):
        """Register CLI arguments for function.

        Accepts the same arguments as ArgumentParser().add_argument(...)
        """
        def wrapper(f):
            if getattr(f, 'cli_args', None) is None:
                f.cli_args = []
            f.cli_args.append((args, kwargs))
            return f
        return wrapper

    def run(self):
        """Parse arguments and run the default action."""
        args = self.parser.parse_args()
        # init logging
        log_level = max(logging.DEBUG, min(logging.CRITICAL, sum(args.verbosity)))
        debug_on = log_level <= logging.DEBUG
        logging.basicConfig(level=log_level)
        kwargs = dict(vars(args))
        # sanitize excess arguments, obiously there are better ways!
        kwargs.pop('action', None)
        kwargs.pop('command', None)
        kwargs.pop('verbosity', None)
        try:
            # callback action
            args.action(**kwargs)
        except Exception as e:
            self.log.error(e, exc_info=debug_on)
            sys.exit(1)
        sys.exit(0)


cli = CLI()


@cli.command('create')
@cli.option('name')
@cli.option('-s', '--size', type=int, choices=range(3))
@cli.option('-t', '--tag', choices=TAGS)
def create_command(name, size, tag):
    """Creates a resource."""
    cli.log.info('creating resource')
    cli.log.info(json.dumps({'name': name, 'size': size, 'tag': tag}))


@cli.command('update')
@cli.option('name')
@cli.option('-s', '--size', type=int, choices=range(3))
@cli.option('-t', '--tag', choices=TAGS)
def update_command(name, size=None, tag=None):
    """Updates a resource."""
    cli.log.info('updating resource')
    cli.log.info(json.dumps({'name': name, 'size': size, 'tag': tag}))


@cli.command('delete')
@cli.option('name')
def delete_command(name):
    """Delete a resource."""
    cli.log.info('deleting resource %s' % name)


@cli.command('list')
def list_command():
    """Lists resources."""
    cli.log.info('listing all resources')


@cli.command('find')
@cli.option('query')
def find_command(query):
    """Finds resources by query."""
    cli.log.info('listing resources matching query %r' % query)


if __name__ == '__main__':
    cli.run()
