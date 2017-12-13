# /usr/bin/env python
# -*- coding:utf8 -*-

import json


def build_response(resp):
    b = json.loads(resp.text)
    if resp.status_code == 200 and b["code"] == 0:
        return b["data"]

    raise AttributeError(b['message'])
