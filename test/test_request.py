from sepulsa.request import SepulsaRequest


def test_to_representation():
    """ test request class that sended to Sepulsa server """
    http_request = SepulsaRequest("username", "password")
    http_request.url = (
        "https://horven-api.sumpahpalapa.com/api/product.json?type=mobile"
    )
    http_request.method = "GET"

    request = http_request.to_representation()
    assert (
        request["url"]
        == "https://horven-api.sumpahpalapa.com/api/product.json?type=mobile"
    )
    assert request["method"] == "GET"
    assert request["data"]
    # make sure header have username key content type and accept
    assert request["headers"]["Content-Type"]
    assert request["headers"]["Accept"]
    assert request["headers"]["Authorization"]
    assert request["timeout"]
