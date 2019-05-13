#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import json

from . import config
from .compat import urlencode
from .compat import urlrequest
from .compat import encode
from .exceptions import APIError


def send_message(channel, message, username=None, icon_url=None):
    text = '```{text}```'.format(text=encode(message))
    _request(
        config.webhook_url, {
            'username': username or config.username,
            'icon_url': icon_url or config.icon_url,
            'channel': channel,
            'text': text,
        },
    )


def _request(url, payload):
    """Make request to Slack's incoming webhooks api."""

    payload = json.dumps(payload)
    data = urlencode({'payload': payload}).encode('utf-8')

    handler = urlrequest.HTTPHandler()
    opener = urlrequest.build_opener(handler)

    request = urlrequest.Request(url)
    response = opener.open(request, data)

    if response.getcode() != 200:
        raise APIError(response.msg)
    return True
