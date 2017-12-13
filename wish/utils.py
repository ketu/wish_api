# /usr/bin/env python
# -*- coding:utf8 -*-

import json


def build_response(resp):
    b = json.loads(resp.text)
    if resp.status_code == 200 and b["code"] == 0:
        if "data" in b:
            return b["data"]
        return b
    raise ValueError(b['message'])
