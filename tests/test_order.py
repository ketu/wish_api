# /usr/bin/env python
# -*- coding:utf8 -*-
from unittest import TestCase
import wish
from .config import client_id,client_secret, access_token, refresh_token

class TestOrder(TestCase):
    def test_wish_order_retrieve(self):
        client = wish.Client(access_token)
        orders = client.order.retrieve_changed_orders()

        print(orders)
        for o in orders:
            print(o["Order"]["order_id"])


