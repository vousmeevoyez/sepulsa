"""
    Excute HTTP Call
    ____________________
"""
import requests

from sepulsa.core.exceptions import FetchError


class RemoteCall:

    def __init__(self, debug=False):
        self.debug = debug

    def fetch(self, request, response):
        """ execute http request """
        try:
            resp = requests.request(**request.to_representation())
        except requests.exceptions.Timeout as error:
            raise FetchError("TIMEOUT", error)
        except requests.exceptions.SSLError as error:
            raise FetchError("SSL_ERROR", error)
        except requests.exceptions.ConnectionError as error:
            raise FetchError("CONNECTION_ERROR", error)
        else:
            response.set(resp)
        return response.to_representation()
