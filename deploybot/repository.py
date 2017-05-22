# -*- coding: utf-8 -*-
from .client import Client


class Repository(Client):
    def list(self):
        client = self.get_client("repositories")
        response = client.get()

        return response.body

    def get(self, repository):
        client = self.get_client("repositories/%s" % repository)
        response = client.get()

        return response.body
