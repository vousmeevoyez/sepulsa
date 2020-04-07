from unittest.mock import Mock, patch
from decimal import Decimal
import pytest

from sepulsa.provider import SepulsaProvider
from sepulsa.core.exceptions import FetchError, StatusCodeError
from sepulsa.exceptions import ProviderError

BASE_URL = "https://horven-api.sumpahpalapa.com/api"


def get_response(request, response, remote_call, method, arguments={}):
    provider = SepulsaProvider(request=request,
                               response=response,
                               remote_call=remote_call,
                               base_url=BASE_URL)

    response = getattr(provider, method)(**arguments)
    return response


def assert_product_item(products):
    for product in products:
        assert product["product_id"]
        assert product["type"]
        assert product["label"]

        if product["operator"] == "":
            assert product["operator"] == ""
        else:
            assert product["operator"]

        assert product["nominal"]
        assert product["price"]
        assert product["enabled"]

        if "field_denom" in product:
            assert product["field_denom"]
        if "field_paket_data" in product:
            assert product["field_paket_data"] is product["field_paket_data"]


@patch("sepulsa.core.remote_call.RemoteCall")
def test_get_products_without_filter(mock_remote_call,
                                     generate_sepulsa_response, setup_request,
                                     setup_response, assert_list):
    """ test get products from sepulsa without any filter """
    sepulsa_response = generate_sepulsa_response("PRODUCTS")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(
        request=setup_request,
        response=setup_response,
        remote_call=mock_remote_call,
        method="get_products",
    )

    assert_list(response)
    assert_product_item(response["list"])


@patch("sepulsa.core.remote_call.RemoteCall")
def test_get_products_with_filter(mock_remote_call, generate_sepulsa_response,
                                  setup_request, setup_response, assert_list):
    """ test get products from sepulsa with filter """
    sepulsa_response = generate_sepulsa_response("PRODUCTS")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(
        request=setup_request,
        response=setup_response,
        remote_call=mock_remote_call,
        method="get_products",
        arguments={"product_type": "mobile"},
    )

    assert_list(response)
    assert_product_item(response["list"])


@patch("sepulsa.core.remote_call.RemoteCall")
def test_get_balance(mock_remote_call, generate_sepulsa_response, setup_request,
                     setup_response):
    """ test get balance from sepulsa """
    sepulsa_response = generate_sepulsa_response("BALANCE")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(
        request=setup_request,
        response=setup_response,
        remote_call=mock_remote_call,
        method="get_balance",
    )

    assert response["balance"]


@patch("sepulsa.core.remote_call.RemoteCall")
def test_get_transaction_history(mock_remote_call, generate_sepulsa_response,
                                 setup_request, setup_response, assert_list):
    """ test get transaction history that created from sepulsa """
    sepulsa_response = generate_sepulsa_response("TRANSACTIONS")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(
        request=setup_request,
        response=setup_response,
        remote_call=mock_remote_call,
        method="get_transaction_history",
    )

    assert_list(response)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_get_transaction_detail(mock_remote_call, generate_sepulsa_response,
                                setup_request, setup_response,
                                assert_transaction_details):
    """ test get transaction detail that created from sepulsa """
    sepulsa_response = generate_sepulsa_response("TRANSACTION_DETAIL")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(
        request=setup_request,
        response=setup_response,
        remote_call=mock_remote_call,
        method="get_transaction_detail",
        arguments={"transaction_id": 1},
    )
    assert_transaction_details(response)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_create_mobile_prepaid_transaction(mock_remote_call,
                                           generate_sepulsa_response,
                                           setup_request, setup_response,
                                           assert_create_transaction):
    """ test create mobile prepaid transaction from sepulsa """
    sepulsa_response = generate_sepulsa_response("MOBILE_PREPAID")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(
        request=setup_request,
        response=setup_response,
        remote_call=mock_remote_call,
        method="create_mobile_prepaid_transaction",
        arguments={
            "customer_number": "08123456789",
            "order_id": "ORDER-001",
            "product_id": 99,
        },
    )
    assert_create_transaction(response)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_inquire_bpjs_kesehatan(mock_remote_call, generate_sepulsa_response,
                                setup_request, setup_response,
                                assert_bpjs_kesehatan):
    """ test inquire bjps kesehatan from sepulsa """
    sepulsa_response = generate_sepulsa_response("INQUIRE_BPJS_KESEHATAN")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(
        request=setup_request,
        response=setup_response,
        remote_call=mock_remote_call,
        method="inquire_bpjs_kesehatan",
        arguments={
            "customer_number": "08123456789",
            "product_id": 99,
            "payment_period": "01",
        },
    )
    assert_bpjs_kesehatan(response)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_create_bpjs_kesehatan_transaction(mock_remote_call,
                                           generate_sepulsa_response,
                                           setup_request, setup_response,
                                           assert_create_transaction):
    """ test create bjps kesehatan from sepulsa """
    sepulsa_response = generate_sepulsa_response("BPJS_KESEHATAN")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(
        request=setup_request,
        response=setup_response,
        remote_call=mock_remote_call,
        method="create_bpjs_kesehatan_transaction",
        arguments={
            "customer_number": "08123456789",
            "order_id": "ORDER-001",
            "product_id": 99,
            "payment_period": "01",
        },
    )
    assert_create_transaction(response)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_inquire_pln_prepaid(mock_remote_call, generate_sepulsa_response,
                             setup_request, setup_response,
                             assert_inquire_pln_prepaid):
    """ test inqiure pln prepaid from sepulsa """
    sepulsa_response = generate_sepulsa_response("INQUIRE_PLN_PREPAID")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(
        request=setup_request,
        response=setup_response,
        remote_call=mock_remote_call,
        method="inquire_pln_prepaid",
        arguments={
            "customer_number": "01428800700",
            "product_id": "25",
        },
    )
    assert_inquire_pln_prepaid(response)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_create_pln_prepaid_transaction(mock_remote_call,
                                        generate_sepulsa_response,
                                        setup_request, setup_response,
                                        assert_create_transaction):
    """ test create pln prepaid from sepulsa """
    sepulsa_response = generate_sepulsa_response("PLN_PREPAID")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(request=setup_request,
                            response=setup_response,
                            remote_call=mock_remote_call,
                            method="create_pln_prepaid_transaction",
                            arguments={
                                "customer_number": "08123456789",
                                "pln_meter_no": "01428800700",
                                "product_id": "25",
                                "order_id": "ORDER-001"
                            })
    assert_create_transaction(response)


@patch("sepulsa.core.remote_call.RemoteCall")
def test_inquire_pln_postpaid(mock_remote_call, generate_sepulsa_response,
                              setup_request, setup_response,
                              assert_inquire_pln_postpaid,
                              assert_pln_postpaid_bills):
    """ test inquire pln postpaid from sepulsa """
    sepulsa_response = generate_sepulsa_response("INQUIRE_PLN_POSTPAID")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(request=setup_request,
                            response=setup_response,
                            remote_call=mock_remote_call,
                            method="inquire_pln_postpaid",
                            arguments={
                                "customer_number": "512345610000",
                                "product_id": 80
                            })
    assert_inquire_pln_postpaid(response)
    assert_pln_postpaid_bills(response["bills"])


@patch("sepulsa.core.remote_call.RemoteCall")
def test_create_pln_postpaid_transaction(mock_remote_call,
                                         generate_sepulsa_response,
                                         setup_request, setup_response,
                                         assert_create_transaction):
    """ test ccreate pln postpaid from sepulsa """
    sepulsa_response = generate_sepulsa_response("PLN_POSTPAID")
    mock_response = setup_response(response=sepulsa_response)
    mock_remote_call.fetch.return_value = mock_response.to_representation()

    response = get_response(request=setup_request,
                            response=setup_response,
                            remote_call=mock_remote_call,
                            method="create_pln_postpaid_transaction",
                            arguments={
                                "customer_number": "512345610000",
                                "product_id": 80,
                                "order_id": "ORDER-001"
                            })
    assert_create_transaction(response)
