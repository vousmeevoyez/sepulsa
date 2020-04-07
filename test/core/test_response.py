"""
    Test Core HTTP response
"""
from unittest.mock import Mock, patch
import pytest

from sepulsa.core.response import HTTPResponse
from sepulsa.core.exceptions import StatusCodeError, InvalidResponseError


def test_validate_success_status_code(setup_http_response):
    # validate successfull http status_code code
    mock_http_response = setup_http_response(200)

    response = HTTPResponse()
    response.set(mock_http_response)

    assert response.validate_status_code()


def test_validate_failed_status_code(setup_http_response):
    # first test error http code with JSON
    mock_http_response = setup_http_response(400)

    with pytest.raises(StatusCodeError):
        response = HTTPResponse()
        response.set(mock_http_response)
        response.validate_status_code()

    mock_http_response = setup_http_response(200)

    response = HTTPResponse()
    response.set(mock_http_response)
    assert response.validate_status_code()


def test_validate_data(setup_http_response):
    mock_http_response = setup_http_response(
        200,
        {
            "data": "Your request has been processed\
        successfully"
        },
    )

    response = HTTPResponse()
    response.set(mock_http_response)

    assert response.validate_data()

    mock_http_response = setup_http_response(200, "request success")

    response = HTTPResponse()
    response.set(mock_http_response)
    assert response.validate_data()

    mock_http_response = Mock()
    # simujlate error parsing json
    mock_http_response.json.side_effect = ValueError

    with pytest.raises(InvalidResponseError):
        response = HTTPResponse()
        response.set(mock_http_response)
        response.validate_data()


def test_to_representation_ok(setup_http_response):
    """ test successfull request """
    mock_http_response = Mock(status_code=200)
    expected_data = {"data": "Your request has been processed successfully"}
    mock_http_response.json.return_value = expected_data

    response = HTTPResponse()
    response.set(mock_http_response)
    assert response.to_representation() == expected_data


def test_to_representation_bad_request(setup_http_response):
    """ test successfull request """
    mock_http_response = Mock(status_code=400)
    expected_data = {"error": "some bad request"}
    mock_http_response.json.return_value = expected_data

    with pytest.raises(StatusCodeError):
        response = HTTPResponse()
        response.set(mock_http_response)
        response.to_representation()


def test_to_representation_internal_error(setup_http_response):
    """ test successfull request """
    mock_http_response = Mock(status_code=500)
    expected_data = {"error": "internal server error"}
    mock_http_response.json.return_value = expected_data

    with pytest.raises(StatusCodeError):
        response = HTTPResponse()
        response.set(mock_http_response)
        response.to_representation()
