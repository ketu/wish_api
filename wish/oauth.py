# /usr/bin/env python
# -*- coding:utf8 -*-
import random
from urllib import parse as urlparse
import requests
import string
import json
from .settings import BASE_URL, BASE_SANDBOX_URL, BASE_ENDPOINT


class Oauth(object):
    authorization_endpoint = "/oauth/authorize"
    access_token_endpoint = BASE_ENDPOINT.rstrip("/") + "/oauth/access_token"
    refresh_token_endpoint = BASE_ENDPOINT.rstrip("/") + "/oauth/refresh_token"

    def __init__(self, client_id, client_secret, redirect_uri, env="PROD"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        if env == "SANDBOX":
            self.base_authorization_url = urlparse.urljoin(BASE_SANDBOX_URL, self.authorization_endpoint)
            self.base_access_token_url = urlparse.urljoin(BASE_SANDBOX_URL, self.access_token_endpoint)
            self.base_refresh_token_url = urlparse.urljoin(BASE_SANDBOX_URL, self.access_token_endpoint)
        else:
            self.base_authorization_url = urlparse.urljoin(BASE_URL, self.authorization_endpoint)
            self.base_access_token_url = urlparse.urljoin(BASE_URL, self.access_token_endpoint)
            self.base_refresh_token_url = urlparse.urljoin(BASE_URL, self.refresh_token_endpoint)

    def make_authorization_url(self, state=None, scope=None):
        u = urlparse.urlparse(self.base_authorization_url)
        if not state:
            state = "".join(random.sample(string.ascii_letters, 32))
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "state": state
        }
        if scope:
            params["scope"] = " ".join(scope)

        query = urlparse.urlencode(params)

        url = urlparse.urlunparse((u.scheme, u.netloc, u.path, u.params, query, u.fragment))
        return url, state

    def prepare_response_body(self, r):
        b = json.loads(r.text)

        if r.status_code == 200 and b["code"] == 0:
            return b["data"]

        raise AttributeError(b['message'])

    def get_access_token(self, authorization_code):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": authorization_code,
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri
        }
        r = requests.post(self.base_access_token_url, data=params)
        return self.prepare_response_body(r)

    def get_access_token_by_refresh_token(self, refresh_token):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
            'grant_type': 'refresh_token'
        }
        r = requests.post(self.base_refresh_token_url, data=params)
        return self.prepare_response_body(r)
