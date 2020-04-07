import pytest
from unittest.mock import Mock, patch

from sepulsa.core.provider import BaseProvider
from sepulsa.core.exceptions import (
    FetchError,
    StatusCodeError,
    InvalidResponseError,
    ResponseError,
)
from sepulsa.exceptions import ProviderError


def test_dict_to_url_query():
    mock_request = Mock()
    mock_response = Mock()
    mock_remote_call = Mock()

    provider = BaseProvider(mock_request, mock_response, mock_remote_call)
    result = provider.dict_to_url_query({"offset": 0, "limit": 100})
    assert result == "?offset=0&limit=100"


def test_provider():
    mock_request = Mock()
    mock_response = Mock()
    mock_remote_call = Mock()

    provider = BaseProvider(mock_request, mock_response, mock_remote_call)
    provider_payload = {
        "url": "https://sandbox.sepulsaindonesia.com/staging/partner",
        "method": "POST",
        "payload": {"recipient_bank": "014", "recipient_account": "1239812390"},
    }

    mock_request_payload = {
        "url": "https://sandbox.sepulsaindonesia.com/staging/partner",
        "method": "POST",
        "data": {"recipient_bank": "014", "recipient_account": "1239812390"},
    }

    mock_request.to_representation.return_value = mock_request_payload

    mock_response_payload = {
        "status": {"code": "000", "message": "Success"},
        "recipient_bank": "014",
        "recipient_account": "1239812390",
        "recipient_name": "John Doe",
        "timestamp": "16-10-2019 09:55:31",
    }

    mock_response.to_representation.return_value = mock_response_payload
    mock_remote_call.fetch.return_value = mock_response_payload

    response = provider.execute(**provider_payload)
    assert response["status"]
    assert response["recipient_bank"]
    assert response["recipient_name"]
    assert response["timestamp"]


def test_provider_with_query_params():
    mock_request = Mock()
    mock_response = Mock()
    mock_remote_call = Mock()

    provider = BaseProvider(mock_request, mock_response, mock_remote_call)
    provider_payload = {
        "url": "https://sandbox.sepulsaindonesia.com/staging/partner/",
        "url_path": "some-url-path",
        "query_params": {"offset": 0, "limit": 100},
        "method": "POST",
        "payload": {"recipient_bank": "014", "recipient_account": "1239812390"},
    }

    mock_request_payload = {
        "url": "https://sandbox.sepulsaindonesia.com/staging/partner",
        "method": "POST",
        "data": {"recipient_bank": "014", "recipient_account": "1239812390"},
    }

    mock_request.to_representation.return_value = mock_request_payload

    mock_response_payload = {
        "status": {"code": "000", "message": "Success"},
        "recipient_bank": "014",
        "recipient_account": "1239812390",
        "recipient_name": "John Doe",
        "timestamp": "16-10-2019 09:55:31",
    }

    mock_response.to_representation.return_value = mock_response_payload
    mock_remote_call.fetch.return_value = mock_response_payload

    response = provider.execute(**provider_payload)
    assert response["status"]
    assert response["recipient_bank"]
    assert response["recipient_name"]
    assert response["timestamp"]


@patch("sepulsa.core.remote_call.RemoteCall")
def test_provider_status_code_error(mock_remote_call, setup_request, setup_response):
    """ simulate provider receive status error """
    mock_remote_call.fetch.side_effect = StatusCodeError

    provider = BaseProvider(setup_request, setup_response, mock_remote_call)
    provider_payload = {
        "url": "https://sandbox.sepulsaindonesia.com/staging/partner",
        "method": "POST",
        "payload": {"recipient_bank": "014", "recipient_account": "1239812390"},
    }

    with pytest.raises(ProviderError):
        provider.execute(**provider_payload)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_provider_invalid_response_error(
    mock_remote_call, setup_request, setup_response
):
    """ simulate provider receive invalid response error """
    mock_remote_call.fetch.side_effect = InvalidResponseError

    provider = BaseProvider(setup_request, setup_response, mock_remote_call)
    provider_payload = {
        "url": "https://sandbox.sepulsaindonesia.com/staging/partner",
        "method": "POST",
        "payload": {"recipient_bank": "014", "recipient_account": "1239812390"},
    }

    with pytest.raises(ProviderError):
        provider.execute(**provider_payload)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_provider_fetch_error(mock_remote_call, setup_request, setup_response):
    """ simulate provider receive fetch error """
    mock_remote_call.fetch.side_effect = FetchError

    provider = BaseProvider(setup_request, setup_response, mock_remote_call)
    provider_payload = {
        "url": "https://sandbox.sepulsaindonesia.com/staging/partner",
        "method": "POST",
        "payload": {"recipient_bank": "014", "recipient_account": "1239812390"},
    }

    with pytest.raises(ProviderError):
        provider.execute(**provider_payload)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_provider_response_error(mock_remote_call, setup_request, setup_response):
    """ simulate provider receive response error """
    mock_remote_call.fetch.side_effect = ResponseError

    provider = BaseProvider(setup_request, setup_response, mock_remote_call)
    provider_payload = {
        "url": "https://sandbox.sepulsaindonesia.com/staging/partner",
        "method": "POST",
        "payload": {"recipient_bank": "014", "recipient_account": "1239812390"},
    }

    with pytest.raises(ProviderError):
        provider.execute(**provider_payload)
