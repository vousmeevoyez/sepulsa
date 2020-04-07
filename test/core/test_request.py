"""
    Test Core Http Request
    ______________
"""
from sepulsa.core.request import HTTPRequest


def test_to_representation():
    """ test method for setup a http request header """
    payload = {"recipient_bank": "014", "recipient_account": "1239812390"}

    http_request = HTTPRequest()
    http_request.url = "https://sandbox.sepulsaindonesia.com/staging/partner"
    http_request.method = "POST"
    http_request.payload = payload

    expected_result = {
        "url": "https://sandbox.sepulsaindonesia.com/staging/partner",
        "method": "POST",
        "data": payload,
        "headers": {"Content-Type": "application/json"},
    }

    request = http_request.to_representation()
    assert request["url"] == expected_result["url"]
    assert request["method"] == expected_result["method"]
    assert request["data"] == expected_result["data"]
    assert request["headers"] == expected_result["headers"]
