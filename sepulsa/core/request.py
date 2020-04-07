"""
    HTTP Request Module
    ______________
"""


class HTTPRequest:
    """
        Base Reusable Request class for any HTTPRequest
        _______________________

        Parameters:
            timeout: int (optional)
                how long untill a request timed out
    """

    def __init__(self, timeout=30):
        self._url = None
        self._header = {}
        self._method = None
        self._payload = {}
        self.timeout = timeout

    @staticmethod
    def _convert_to_header_convention(key):
        """
            convert python snakecase syntax to PascalCase with dash (-)
            ex: convert content_type to Content-Type
            ______________
            Parameters:
                key: string

        """
        # first convert key into Capitalize
        capitalize = key.title()
        # second convert underscore into dash
        underscore = capitalize.replace("_", "-")
        return underscore

    def to_representation(self):
        """
            configure right http header and convert Http request Object into representable dict
            ______________
            Return:
                url: string
                method: string
                data: string
                headers: string
                timeout: int

        """
        # convert object into parsable data
        self.setup_header()
        return {
            "url": self._url,
            "method": self._method,
            "data": self._payload,
            "headers": self._header,
            "timeout": self.timeout,
        }

    def setup_header(self, **config):
        """
            setup HTTP request header
            ______________
            Parameters:
                args:
                kwargs:
        """
        self._header["Content-Type"] = "application/json"

    @property
    def payload(self):
        """
            get HTTP request payload
            ______________
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
            set HTTP request payload
            ______________
        """
        self._payload = payload

    @property
    def url(self):
        """
            get HTTP request url
            ______________
        """
        return self._url

    @url.setter
    def url(self, url):
        """
            set HTTP request url
            ______________
        """
        self._url = url

    @property
    def method(self):
        """
            get HTTP request method
            ______________
        """
        return self._method

    @method.setter
    def method(self, method):
        """
            set HTTP request method
            ______________
        """
        self._method = method
