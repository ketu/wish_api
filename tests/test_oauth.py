# /usr/bin/env python
# -*- coding:utf8 -*-
from unittest import TestCase
import wish
import json

from .config import client_id,client_secret, access_token, refresh_token

class TestOauth(TestCase):
    def test_wish_client_oauth(self):
        oauth = wish.Oauth(client_id, client_secret, "https://127.0.0.1")
        authorization_url, state = oauth.make_authorization_url()
        print(authorization_url)

        token = oauth.get_access_token("72a349e1f00efb45d0a19")


