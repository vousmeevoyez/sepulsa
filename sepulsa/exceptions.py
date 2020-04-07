from sepulsa.core.exceptions import BaseError

# PROVIDER ERROR
class ProviderError(BaseError):
    """
        high level error that abstract status code response and other things
        so the client only dealing with this error instead of other error
    """
