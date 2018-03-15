# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource

__all__ = ["Notification"]


class Notification(Resource):
    """
    notifications
    """

    def fetch_unviewed(self, **kwargs):
        """
        Fetch Notifications
        Returns a list of all your unviewed notifications.
        If you have a high number of notifications the response will be paginated.
        The response will contain the URL for fetching the next page of notifications, as well as the previous page.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/noti/fetch-unviewed
        :param kwargs:
        :return:
        """

        return self.client.execute("noti/fetch-unviewed", "GET", kwargs)

    def mark_as_viewed(self, **kwargs):
        """
        Mark a notification as viewed
        Marks a notification as viewed

        HTTP Request Type: POST

        Definition
        GET https://merchant.wish.com/api/v2/noti/mark-as-viewed
        :param kwargs:
        :return:
        """
        return self.client.execute("noti/mark-as-viewed", "GET", kwargs)

    def count_unviewed(self):
        """
        Get the unviewed notification count
        Get the count of unviewed notification count

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/noti/get-unviewed-count
        :param kwargs:
        :return:
        """
        return self.client.execute("noti/get-unviewed-count", "GET")

    def announcement(self):
        """
        Fetch Announcements
        Fetch the Announcements

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/fetch-bd-announcement
        :return:
        """
        return self.client.execute("fetch-bd-announcement", "GET")

    def system_notification(self):
        """
        Fetch system update notifications
        Fetch system update notifications

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/fetch-sys-updates-noti
        :return:
        """
        return self.client.execute("fetch-sys-updates-noti", "GET")

    def count_infractions(self):
        """
        Infractions count
        Get the count of infractions need the attention of the merchant

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/count/infractions
        :return:
        """
        return self.client.execute("count/infractions", "GET")

    def fetch_infractions(self, **kwargs):
        """
        Fetch infractions
        Fetch infraction links that need the attention of the merchant

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/get/infractions
        :param kwargs:
        :return:
        """
        return self.client.execute("get/infractions", "GET", kwargs)
