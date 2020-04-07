"""
    Sepulsa Client Builder
"""
from sepulsa.request import SepulsaRequest
from sepulsa.response import SepulsaResponse
from sepulsa.provider import SepulsaProvider
from sepulsa.core.remote_call import RemoteCall


def build_client(base_url, username, password):
    """" combine request response and remote call into provider """
    # we need to build request
    request = SepulsaRequest(username, password)
    response = SepulsaResponse()
    remote_call = RemoteCall()
    client = SepulsaProvider(
        base_url=base_url, request=request, response=response, remote_call=remote_call
    )
    return client
