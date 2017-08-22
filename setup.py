# -*- coding: utf-8 -*-
"""crud-cli setup.py"""

from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='crud-cli',
    version='0.1.0',
    description='a cli application to manage resources using cli',
    long_description=readme(),
    license='MIT',
    author='Lukas Šupienis',
    author_email='lukassup@yahoo.com',
    keywords='python basic cli crud skeleton',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    url='https://github.com/lukassup/crud-cli',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'crud-cli = crud_cli:cli.run',
        ],
    },
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
)
