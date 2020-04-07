"""
    HTTP Response
    __________________
    base reusable class for various HTTP response
"""

from sepulsa.core.exceptions import InvalidResponseError, StatusCodeError


class HTTPResponse:
    """
        Base Reusable Response class for any HTTPResponse
        _______________________
    """

    wrapper_key = None  # used to unpack response

    ACCEPTED_HTTP_STATUS_CODE = [200]

    def __init__(self):
        self.data = {}
        self.http_status = None

    def set(self, response):
        # unpack response header
        self.http_status = response.status_code
        # parse response and load it into property
        self.data = self._parse(response)

    def _extract(self, data):
        """
            method to unwrap nested response so it much easy to consume
            ______________________
            Parameters:
                data: dictionary

            Return:
                result: dictionary
                    unwrapped response
        """
        result = data

        if self.wrapper_key is not None:
            if self.wrapper_key in data:
                result = data[self.wrapper_key]
        return result

    def _parse(self, response_object):
        """
            method to convert response into JSON
            ______________________
            Parameters:
                data: dictionary

            Return:
                result: dictionary
                    json response

            Raised:
                InvalidResponseError:
                    if response from server is not json raise this
        """
        try:
            response = response_object.json()
        except ValueError as error:
            raise InvalidResponseError("FAILED_DECODE_JSON", error)
        # end try
        return response

    def validate_status_code(self):
        """
            validate response status code
            ______________________
            Return:
                result: boolean
                    true it means valid

            Raised:
                StatusCodeError:
                    if status code from server is not 200
        """
        status_code = self.http_status
        if status_code not in self.ACCEPTED_HTTP_STATUS_CODE:
            # later should check whether status code valid or not !
            raise StatusCodeError("RESPONSE_ERROR", self.data)
        return True

    def validate_data(self):
        """
            validate response data
            by default it do nothing except return boolean
            inherited class must modify this to according their business rule
            ______________________
        """
        return True

    def validate(self):
        """ wrapper method to validate everything """
        self.validate_status_code()
        self.validate_data()

    def to_representation(self):
        """
            validate http response
            convert Http response Object into representable dict
            and unpack response if needed
            ______________
            Return:
                response: dictionary

            Raise:
                StatusCodeError
                InvalidResponseError
        """
        self.validate()
        return self._extract(self.data)
