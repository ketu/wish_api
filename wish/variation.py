# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource

__all__ = ["Variation"]


class Variation(Resource):
    def create(self, product_data):
        """
        Create a Product Variation
        To add a new variation to a product you can create a product variation.
         For example, a product has sizes Large and Extra-Large and you wanted to add size Medium, you would create a new product variation with this API.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/variant/add
        :param product_data:
        :return:
        """
        return self.client.execute("variant/add", "POST", product_data)

    def retrieve(self, **kwargs):
        """
        Retrieve a Product Variation
        Retrieves the details of an existing product variation.
        Provide the SKU of the product variation and Wish will return details about the corresponding product variation.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/variant
        :param kwargs:
        :return:
        """
        return self.client.execute("variant", "GET", kwargs)

    def update(self, update_data):
        """
        Update a Product Variation
        Updates the specified variation by updating the attributes of the parameters passed in the request.
        Any attribute not provided will be left unchanged.

        This request can only update attributes specific to variations and cannot be used to update any attribute of a Product.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/variant/update
        :param update_data:
        :return:
        """
        return self.client.execute("variant/update", "POST", update_data)

    def change_sku(self, **kwargs):
        """
        Change a Product Variation's SKU
        Change a variantion's unique identifier, the new identifier must also be unique within all SKUs of the merchant

        HTTP Request Type: POST

        Definition
        :param kwargs:
        :return:
        """
        return self.client.execute("variant/change-sku", "POST", kwargs)

    def enable(self, **kwargs):
        """
        Enable a Product Variation
        Enable a product variation. This marks the product variation available for sale.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/variant/enable
        :param kwargs:
        :return:
        """
        return self.client.execute("variant/enable", "POST", kwargs)

    def disable(self, **kwargs):
        """
        Disable a Product Variation
        Disable a product variation. This marks the product variation unavailable for sale.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/variant/disable
        :param kwargs:
        :return:
        """
        return self.client.execute("variant/disable", "POST", kwargs)

    def update_inventory(self, **kwargs):
        """
        Update Inventory
        Update inventory for a product variation.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/variant/update-inventory
        :param update_data:
        :return:
        """
        return self.client.execute("variant/update-inventory", "POST", kwargs)

    def list(self, **kwargs):
        """
        List all Product Variations
        Returns a list of all your product variations currently on the Wish platform.
        This API is useful to paginate through all the SKUs that you have uploaded to Wish.
        If the number of results is too large the full result set may require pagination.
        HTTP Request Type: GET
        Definition
        GET https://merchant.wish.com/api/v2/variant/multi-get
        :param kwargs:
        :return:
        """
        return self.client.execute("variant/multi-get", "GET", kwargs)
