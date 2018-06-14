#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

try:
    # Python 3.x
    from urllib.parse import urlencode
    import urllib.request as urlrequest
except ImportError:
    # Python 2.x
    from urllib import urlencode  # noqa
    import urllib2 as urlrequest  # noqa
