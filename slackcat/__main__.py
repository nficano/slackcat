#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import sys

import slack
from ioutil import Stream


def main():
    """slackcat reads a file and sends it to the a slack channel or user. If
    the file is a UNIX domain socket or file path, slackcat reads it until EOF.
    """

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('channel', help='output "#channel" or @user')
    parser.add_argument('source', help='source', nargs='?', default=None)
    parser.add_argument(
        '-f', '--follow', action='store_true', help=(
            'The follow option causes slackcat to not stop when end of file '
            'is reached, but rather to wait for additional data to be '
            'appended to the input.'
        ),
    )
    args = parser.parse_args()
    is_piped = not sys.stdin.isatty()

    if is_piped or args.source:
        slackcat(args.channel, filepath=args.source, ignore_eof=args.follow)
    else:
        parser.print_help()
        exit(1)


def slackcat(channel, filepath=None, ignore_eof=False):
    if filepath and ignore_eof:
        with open(filepath) as fh:
            with Stream(fh) as stream:
                try:
                    for line in stream:
                        slack.send_message(channel, line)
                except KeyboardInterrupt:
                    exit(0)

    elif filepath and not ignore_eof:
        with open(filepath) as fh:
            slack.send_message(channel, fh.read())

    elif not filepath and ignore_eof:
        with Stream(sys.stdin) as stream:
            try:
                for line in stream:
                    slack.send_message(channel, line)
            except KeyboardInterrupt:
                exit(0)
    else:
        slack.send_message(channel, sys.stdin.read())


if __name__ == '__main__':
    main()
