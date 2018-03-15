# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource

__all__ = ["Product"]


class Product(Resource):
    def create(self, product_data):
        """
        Create a Product
        Use the endpoint to create a new product.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/product/add
        :param product_data:
        :return:
        """
        return self.client.execute("product/add", "POST", product_data)

    def retrieve(self, **kwargs):
        """
        Retrieve the details about a product which exists on the Wish platform.
        You must have the unique product Id or the parent sku that was returned upon product creation.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/product
        :param kwargs:
        :return:
        """
        return self.client.execute("product", "GET", kwargs)

    def update(self, update_data):
        """
        Update a Product
        Updates the specified product with the parameters passed in the request. 
        Any attribute not provided will be left unchanged. For example, 
        if you pass the name parameter we will update the name of the product and leave everything else unchanged.
        
        This request can only update attributes specific to products and cannot be used to update anything to do with the product variations of a product.
        
        HTTP Request Type: POST
        
        Definition
        POST https://merchant.wish.com/api/v2/product/update
        :param update_data:
        :return:
        """
        return self.client.execute("product/update", "POST", update_data)

    def enable(self, **kwargs):
        """
        Enable a Product
        Enable a product and all of its product variations. This marks the product available for sale.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/product/enable
        :param kwargs:
        :return:
        """
        return self.client.execute("product/enable", "POST", kwargs)

    def disable(self, **kwargs):
        """
        Disable a Product
        Disable a product and all of its product variations. This marks the product unavailable for sale.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/product/disable

        :param kwargs:
        :return:
        """
        return self.client.execute("product/disable", "POST", kwargs)

    def list(self, **kwargs):
        """
        List all Products
        This API will be changed starting Oct. 24, 2016. Please switch to the batch download API to download all Products.

        Returns a list of all your products currently on the Wish platform.
        If you have a high number of products the response will be paginated.
        The response will contain the URL for fetching the next page of products.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/product/multi-get


        :param kwargs:
        :return:
        """
        return self.client.execute("product/multi-get", "GET", kwargs)

    def remove_extra_images(self, **kwargs):
        """
        Remove Extra Images from a Product
        This removes all the extra images from the product.
        The main product image and variation images will not be affected.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/product/remove-extra-images
        :param kwargs:
        :return:
        """
        return self.client.execute("product/remove-extra-images", "GET", kwargs)

    def update_shipping_prices(self, **kwargs):
        """
        Edit Shipping Price of a Product
        This edits the shipping prices of a product to a specific country.

        The merchant's shipping settings for this country must exist to indicate that the merchant supports this country.

        You can set field 'enabled' to false to indicate that the product is disabled for that country.
        Users from a disabled country will not be able to buy the product.
        To re-enable a prodcut, set the 'enabled' field to true or set the shipping price without the 'enabled' field.

        If you are part of the Wish Express program, you can set the field 'wish_express' to
        indicate whether the product should be enrolled in Wish Express for this country.
        You cannot disable Wish Express if the product is promoted. If you make a mistake, you must correct it immediately.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/product/update-shipping
        :param kwargs:
        :return:
        """
        return self.client.execute("product/update-shipping", "POST", kwargs)

    def update_multi_shipping_prices(self, **kwargs):
        """
        Edit Shipping Prices of a Product
        This edits the shipping prices of a product.

        The merchant's shipping settings for this country must exist to indicate that the merchant supports this country.

        If you are enrolled in the Wish Express program, you can specify Wish Express countries to enable for the product.
        To disable Wish Express countries, please use the Merchant Dashboard.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/product/update-multi-shipping
        :param kwargs:
        :return:
        """
        return self.client.execute("product/update-multi-shipping", "POST", kwargs)

    def get_shipping_prices(self, **kwargs):
        """
        Get Shipping Prices of a Product
        Retrieve the shipping price of a product to a specific country and a flag indicating if the product is enabled for the country.

        If merchant's shipping setting indicates that merchant does not ship to this country, the result will be an error.

        If merchant's shipping setting indicates that he/she uses the product variation level shipping prices, the result will be an error.
        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/product/get-shipping


        :param kwargs:
        :return:
        """
        return self.client.execute("product/get-shipping", "GET", kwargs)

    def get_all_shipping_prices(self, **kwargs):
        """
        Get All Shipping Prices of a Product
        Retrieve the shipping prices of a product to all enabled countries.

        If merchant's shipping setting indicates that merchant ships worldwide, the result will be an error.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/product/get-all-shipping
        :param kwargs:
        :return:
        """
        return self.client.execute("product/get-all-shipping", "GET", kwargs)

    def list_shipping_prices(self, **kwargs):
        """
        Get Shipping Prices of Many Products
        Retrieve the shipping prices of many products to all enabled countries.

        If merchant's shipping setting indicates that merchant ships worldwide, the result will be an error.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/product/get-products-shipping
        :param kwargs:
        :return:
        """
        return self.client.execute("product/get-products-shipping", "GET", kwargs)

    def create_download_job(self, **kwargs):
        """
        Start a Batch Product Download
        Call this to begin downloading a CSV file of your Products.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/product/create-download-job
        :param kwargs:
        :return:
        """
        return self.client.execute("product/create-download-job", "POST", kwargs)

    def get_download_job_status(self, **kwargs):
        """
        Get the Status of Your Batch Product Download
        Call this to get a progress update for your batch Product download.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/product/get-download-job-status


        :param kwargs:
        :return:
        """
        return self.client.execute("product/get-download-job-status", "POST", kwargs)

    def cancel_download_job_status(self, **kwargs):
        """
        Cancel Your Batch Product Download
        Call this to cancel a batch Product download that is pending or running.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/product/cancel-download-job


        :param kwargs:
        :return:
        """
        return self.client.execute("product/cancel-download-job", "POST", kwargs)
