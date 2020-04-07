"""
    Exceptions
    ________________
"""


class BaseError(Exception):
    """ Base Error for all Sepulsa Library """

    def __init__(self, message=None, original_exception=None):
        super().__init__(original_exception)
        self.original_exception = original_exception
        self.message = message


# HTTP Response Exceptions


class StatusCodeError(BaseError):
    """ error raised related to status code error"""


class InvalidResponseError(BaseError):
    """ Error raised when server return something that can be parsed
    by response """


class ResponseError(BaseError):
    """ Error raised when response error it can be failed / invalid """


class DuplicateRequestError(BaseError):
    """ Error raised when client try send request that already received or processed """


#  FETCH ERROR
class FetchError(BaseError):
    """ raised when error fetching request or response from server """
