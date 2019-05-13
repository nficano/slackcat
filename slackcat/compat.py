#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

try:
    # Python 3.x
    from urllib.parse import urlencode
    import urllib.request as urlrequest

    def encode(s, decode='unicode_escape', encode='utf-8'):
        return s

except ImportError:
    # Python 2.x
    from urllib import urlencode  # noqa
    import urllib2 as urlrequest  # noqa

    def encode(s, decode='unicode_escape', encode='utf-8'):
        return s.decode(decode).encode(encode)

