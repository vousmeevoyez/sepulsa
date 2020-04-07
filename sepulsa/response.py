"""
    Sepulsa Response
    __________________
"""
from urllib.parse import urlparse, parse_qs

from sepulsa.core.response import HTTPResponse
from sepulsa.core.exceptions import (
    ResponseError,
    DuplicateRequestError,
    InvalidResponseError,
    StatusCodeError,
)


class SepulsaResponse(HTTPResponse):

    ACCEPTED_HTTP_STATUS_CODE = [200, 201]

    def _parse(self, response_object):
        """
            because sometime the response is not json we need to be able to
            handle it
        """
        try:
            response = super()._parse(response_object)
        except InvalidResponseError:
            # extract the plain text response
            response = response_object.text
        # end try
        return response

    @staticmethod
    def _validate_sepulsa_status(response):
        """
            Validate sepulsa status
            ________________
            Parameters:
                response :
                    response from sepulsa server

            Return:
                response :
                    response from sepulsa server

            Raised:
                FailedResponseError :
                    if response from sepulsa server contain status code other than
                    accepted status code we raise this

        """
        # because not all response from respulsa contain repsonse_code we need
        # to check it first
        if "response_code" in response:
            status_code = response["response_code"]
            # accepted code only 00 or 10
            if status_code not in ["00", "10"]:
                raise ResponseError("STATUS_FAILED", original_exception=response)
        return response

    @staticmethod
    def _trim_response(response):
        """
            trim sepulsa response
            ________________
            Parameters:
                response :
                    response from sepulsa server

            Return:
                trimmed_response :
                    trimmed response from sepulsa server without status object
        """
        if "response_code" in response:
            response.pop("response_code")
        return response

    @staticmethod
    def _extract_query_params_from_url(url):
        result = urlparse(url)
        return parse_qs(result.query)

    def _transform_hateoas(self, response):
        """
            transform sepulsa paginated response
            self, first, last, next to current, first, last
            ________________
            Parameters:
                response :
                    response from sepulsa server

            Return:
                trimmed_response :
                    trimmed response from sepulsa server without status object
        """
        pagination = ["self", "first", "last", "next"]
        skipped = ["list"]
        if any(key in pagination for key in response):
            for key in response:
                if key not in skipped:
                    response[key] = self._extract_query_params_from_url(response[key])
        return response

    def validate_status_code(self):
        """ re raise from parent class and convert it as response error instead
        of status code error from sepulsa http status code """
        try:
            # first validate status any response
            response = super().validate_status_code()
        except StatusCodeError as error:
            raise ResponseError("RESPONSE_FAILED", error.original_exception)
        return response

    def validate_data(self):
        """ validate sepulsa status """
        try:
            # first validate status any response
            self._validate_sepulsa_status(self.data)
            trimmed_response = self._trim_response(self.data)
            transformed_response = self._transform_hateoas(trimmed_response)
            self.data = transformed_response
        except ResponseError as error:
            raise ResponseError("RESPONSE_FAILED", error.original_exception)
