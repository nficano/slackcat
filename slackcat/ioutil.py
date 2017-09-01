#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stream(object):
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.file.close()

    def __iter__(self):
        return self

    def next(self):
        line = self.file.readline()

        if not line or line == '':
            raise StopIteration

        return line
