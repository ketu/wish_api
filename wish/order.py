# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource

__all__ = ["Order"]


class Order(Resource):
    def retrieve(self, **kwargs):
        """
        Retrieve an Order
        Retrieves the details of an existing order.
        Supply the unique identifier for the order and if one exists this API will return the corresponding order.
        Each order will have all the information you need to fulfill it
        HTTP Request Type: GET
        Definition GET https://sandbox.merchant.wish.com/api/v2/order
        :param kwargs:
        :return:
        """
        return self.client.execute("order", "GET", kwargs)

    def retrieve_changed_orders(self, **kwargs):
        """
        Retrieve Recently Changed Orders
        This API will be changed starting Oct. 24, 2016. Please switch to the batch download API to download all Orders.

        Returns all orders that have changed state since the date and time requested.
        Use this API to keep your orders processing system in sync with Wish.
        This API takes a parameter 'since' and returns all orders that were updated since this time.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/order/multi-get

        :param kwargs:
        :return:
        """
        return self.client.execute("order/multi-get", "GET", kwargs)

    def retrieve_unfulfilled_orders(self, **kwargs):
        """
        Retrieve Unfulfilled Orders
        Returns all orders that currently require fulfillment.
        This API takes no parameters but may require pagination if the number of orders is too large.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/order/get-fulfill
        :param kwargs:
        :return:
        """
        return self.client.execute("order/get-fulfill", "GET", kwargs)

    def fulfill_order(self, **kwargs):
        """
        Fulfill an Order
        Fulfills an order in the Wish system.
        Call this API once you have shipped the item to the recipient.
        Wish will notify the user their order has been shipped upon completion of this request.
        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/order/fulfill-one
        :param kwargs:
        :return:
        """
        return self.client.execute("order/fulfill-one", "POST", kwargs)

    def cancel_order(self, **kwargs):
        """
        Refund/Cancel an Order
        Refund/Cancel an order in the Wish system.
        Call this API if you cannot fulfill the order for any reason.
        Wish will notify the user their order has been cancelled shipped and refund them upon completion of this request.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/order/refund
        :param kwargs:
        :return:
        """
        return self.client.execute("order/refund", "POST", kwargs)

    def modify_tracking(self, **kwargs):
        """
        Modify Tracking of a Shipped Order
        Update tracking information about an order.
        Call this to change the tracking number or provider for an order that has already been marked shipped.
        :param kwargs:
        :return:
        """
        return self.client.execute("order/modify-tracking", "POST", kwargs)

    def change_shipping(self, **kwargs):
        """
        Modify Shipping Address of an Order Before Shipping
        Change shipping information for an order.
        Call this to change the shipping address for an order that has not been marked shipped.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/order/change-shipping
        :param kwargs:
        :return:
        """
        return self.client.execute("order/change-shipping", "POST", kwargs)

    def create_download_job(self, **kwargs):
        """
        Start a Batch Order Download
        Call this to begin downloading a CSV file of your Orders.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/order/create-download-job


        :param kwargs:
        :return:
        """
        return self.client.execute("order/create-download-job", "POST", kwargs)

    def get_download_job_status(self, **kwargs):
        """
        Get the Status of Your Batch Order Download
        Call this to get a progress update for your batch Order download.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/order/get-download-job-status


        :param kwargs:
        :return:
        """
        return self.client.execute("order/get-download-job-status", "POST", kwargs)

    def cancel_download_job(self, **kwargs):
        """
        Cancel Your Batch Order Download
        Call this to cancel a batch Order download that is pending or running.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/order/cancel-download-job
        :param kwargs:
        :return:
        """
        return self.client.execute("order/cancel-download-job", "POST", kwargs)
