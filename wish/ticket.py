# /usr/bin/env python
# -*- coding:utf8 -*-

from .resource import Resource

__all__ = ["Ticket"]


class Ticket(Resource):

    def retrieve(self, **kwargs):
        """
        Retrieve a Ticket
        Retrieves the details of an existing ticket.
        Supply the unique identifier for the ticket and if one exists this API will return the corresponding ticket.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/ticket
        :param kwargs:
        :return:
        """
        return self.client.execute("ticket", "GET", kwargs)

    def list_waiting_tickets(self, **kwargs):
        """
        List all Tickets Awaiting You
        Returns a list of all your open tickets currently on the Wish platform awaiting your response. If you have a high number of tickets the response will be paginated. The response will contain the URL for fetching the next page of tickets, as well as the previous page.

        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/ticket/get-action-required
        :param kwargs:
        :return:
        """
        return self.client.execute("ticket/get-action-required", "GET", kwargs)

    def reply(self, **kwargs):
        """
        Reply to a Ticket
        Send a reply for a ticket. Wish will notify the user of the reply if required.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/ticket/reply
        :param kwargs:
        :return:
        """
        return self.client.execute("ticket/reply", "POST", kwargs)

    def close(self, **kwargs):
        """
        Close a Ticket
        Close a order in the Wish system. Call this API if you answered all the users questions to their statisification.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/ticket/close
        :param kwargs:
        :return:
        """
        return self.client.execute("ticket/close", "POST", kwargs)


    def appeal(self, **kwargs):
        """
        Appeal to Wish Support for Ticket
        Appeal to wish support for a ticket. Call this if the user has questions you are unable to answer.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/ticket/appeal-to-wish-support
        :param kwargs:
        :return:
        """
        return self.client.execute("ticket/appeal-to-wish-support", "POST", kwargs)

    def reopen(self, **kwargs):
        """
        Re-open a Ticket
        Re-open a ticket on the Wish platform. Call this API if something happens to make the ticket relevant again.

        HTTP Request Type: POST

        Definition
        POST https://merchant.wish.com/api/v2/ticket/re-open
        :param kwargs:
        :return:
        """

        return self.client.execute("ticket/re-open", "POST", kwargs)

