"""
    Sepulsa Request
    __________________
"""
import base64
import json
from sepulsa.core.request import HTTPRequest


class SepulsaRequest(HTTPRequest):
    """ Request Class for handling Sepulsa Request """

    def __init__(self, username, password, timeout=30):
        super().__init__(timeout)
        self.username = username
        self.password = password

    def setup_header(self, **config):
        credentials = f"{self.username}:{self.password}"
        encoded_credentials = \
            base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

        self._header["Content-Type"] = "application/json"
        self._header["Accept"] = "application/json"
        self._header["Authorization"] = "Basic {}".format(encoded_credentials)

    def to_representation(self):
        response = super().to_representation()
        # convert data into json
        response["data"] = json.dumps(response["data"])
        return response
