#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as fh:
    readme = fh.read()

with open('LICENSE') as fh:
    license = fh.read()

setup(
    name='slackcat',
    version='1.0.0',
    author='Nick Ficano',
    author_email='nficano@gmail.com',
    packages=['slackcat'],
    url='https://github.com/nficano/slackcat',
    license=license,
    entry_points={
        'console_scripts': [
            'slackcat = slackcat.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    description='Pipe command output to Slack from your terminal!',
    long_description=readme,
    zip_safe=True,
)
