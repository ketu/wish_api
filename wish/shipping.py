# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource

__all__ = ["Shipping"]


class Shipping(Resource):
    def get_confirmed_delivery_countries(self):
        """
        Get Countries that Require Confirmed Delivery
        Get a list of country codes for countries that require Confirmed Delivery for the Confirmed Delivery Policy.

        For more information about the Confirmed Delivery Policy, click here.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/order/get-confirmed-delivery-countries
        :return:
        """
        return self.client.execute("order/get-confirmed-delivery-countries", "POST")

    def get_confirmed_delivery_shipping_carriers(self, **kwargs):
        """
        Get Confirmed Delivery Shipping Carriers For Country
        Get a list of Shipping Carriers that provide tracking with Delivery Confirmation to a specified country.

        For a full list of these Shipping Carriers, click here.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/order/get-confirmed-delivery-shipping-carriers-for-country

        :param kwargs:
        :return:
        """
        return self.client.execute("order/get-confirmed-delivery-shipping-carriers-for-country", "POST", kwargs)

    def get_shipping_carriers(self):
        """
        Accepted Shipping Providers
        This fetches all accepted shipping providers.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/get-shipping-carriers
        :return:
        """
        return self.client.execute("get-shipping-carriers", "GET")

    def get_shipping_settings(self):
        """
        Get Merchant Shipping Settings
        Retrieve merchant's shipping settings

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/product/get-shipping-setting
        :return:
        """
        return self.client.execute("product/get-shipping-setting", "GET")
