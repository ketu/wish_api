# /usr/bin/env python
# -*- coding:utf8 -*-

__all__ = ["Resource"]


class Resource(object):
    def __init__(self, client):
        self.client = client
