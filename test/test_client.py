"""
    We test integration between Request + Response + Remote Call + Provider
    class
    so we only mock external modules 'requests'
"""
import uuid
import pytest

from unittest.mock import patch
from sepulsa import build_client

USERNAME = "sepulsausername"
PASSWORD = "sepulsapassword"
BASE_URL = "https://horven-api.sumpahpalapa.com/api"


@patch("requests.request")
def test_get_all_products(mock_request, generate_sepulsa_response, assert_list):
    """ get real all products data from sepulsa """
    response = generate_sepulsa_response("PRODUCTS")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.get_products()
    assert_list(response)


@patch("requests.request")
def test_create_mobile_prepaid_transaction(mock_request,
                                           generate_sepulsa_response,
                                           assert_create_transaction):
    """ get real all products data from sepulsa """
    response = generate_sepulsa_response("MOBILE_PREPAID")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.create_mobile_prepaid_transaction(
        customer_number="081234567890",
        product_id=99,
        order_id=str(uuid.uuid4()))
    assert_create_transaction(response)


@patch("requests.request")
def test_inquire_bpjs_kesehatan(mock_request, generate_sepulsa_response,
                                assert_bpjs_kesehatan):
    """ inquire bpjs kesehatan from sepulsa """
    response = generate_sepulsa_response("INQUIRE_BPJS_KESEHATAN")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.inquire_bpjs_kesehatan(customer_number="0000001430071801",
                                             product_id=34,
                                             payment_period="01")
    assert_bpjs_kesehatan(response)


@patch("requests.request")
def test_create_bpjs_kesehatan_transaction(mock_request,
                                           assert_create_transaction,
                                           generate_sepulsa_response):
    """ get create bpjs kesehatan from sepulsa """

    response = generate_sepulsa_response("BPJS_KESEHATAN")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.create_bpjs_kesehatan_transaction(
        customer_number="0000001430071801",
        product_id=34,
        payment_period="01",
        order_id=str(uuid.uuid4()))
    assert_create_transaction(response)


@patch("requests.request")
def test_inquire_pln_prepaid(mock_request, assert_inquire_pln_prepaid,
                             generate_sepulsa_response):
    """ get inquire pln prepaid from sepulsa """
    response = generate_sepulsa_response("INQUIRE_PLN_PREPAID")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.inquire_pln_prepaid(customer_number="01428800700",
                                          product_id=25)
    assert_inquire_pln_prepaid(response)


@patch("requests.request")
def test_create_pln_prepaid_transaction(mock_request, assert_create_transaction,
                                        generate_sepulsa_response):
    """ create pln prepaid transaction from sepulsa """
    response = generate_sepulsa_response("PLN_PREPAID")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.create_pln_prepaid_transaction(
        customer_number="08123456789",
        pln_meter_no="01428800700",
        product_id=25,
        order_id=str(uuid.uuid4()))
    assert_create_transaction(response)


@patch("requests.request")
def test_inquire_pln_postpaid(mock_request, assert_inquire_pln_postpaid,
                              generate_sepulsa_response):
    """ inquire pln postpaid from sepulsa """
    response = generate_sepulsa_response("INQUIRE_PLN_POSTPAID")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.inquire_pln_postpaid(
        customer_number="512345610000",
        product_id=80,
    )
    assert_inquire_pln_postpaid(response)


@patch("requests.request")
def test_create_pln_postpaid_transaction(mock_request,
                                         assert_create_transaction,
                                         generate_sepulsa_response):
    """ create pln postpaid from sepulsa """
    response = generate_sepulsa_response("PLN_POSTPAID")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.create_pln_postpaid_transaction(
        customer_number="512345610000",
        product_id=80,
        order_id=str(uuid.uuid4()))
    assert_create_transaction(response)


@patch("requests.request")
def test_inquire_telkom_bill(mock_request, assert_inquire_telkom_bill,
                             generate_sepulsa_response):
    """ inquire telkom bill from sepulsa """
    response = generate_sepulsa_response("INQUIRE_TELKOM")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.inquire_telkom_bill(customer_number="0218800007",
                                          product_id=82)
    assert_inquire_telkom_bill(response)


@patch("requests.request")
def test_create_telkom_bill_transaction(mock_request, assert_create_transaction,
                                        generate_sepulsa_response):
    """ create telkom bill transaction from sepulsa """
    response = generate_sepulsa_response("TELKOM")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.create_telkom_bill_transaction(
        customer_number="0218800007", product_id=82, order_id=str(uuid.uuid4()))
    assert_create_transaction(response)


@patch("requests.request")
def test_get_pdam_operators(mock_request, assert_pdam_operators,
                            generate_sepulsa_response):
    """ get all pdam operators from sepulsa """
    response = generate_sepulsa_response("PDAM_OPERATOR")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.get_pdam_operators(product_id=87)
    assert_pdam_operators(response)


@patch("requests.request")
def test_inquire_pdam_bill(mock_request, assert_inquire_pdam,
                           generate_sepulsa_response):
    """ inquire pdam bills from sepulsa """
    response = generate_sepulsa_response("INQUIRE_PDAM")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.inquire_pdam_bill(customer_number="1998900001",
                                        product_id=87,
                                        operator_code="pdam_aetra")
    assert_inquire_pdam(response)


@patch("requests.request")
def test_create_pdam_bill_transaction(mock_request, assert_create_transaction,
                                      generate_sepulsa_response):
    """ create pdam bill transaction from sepulsa """
    response = generate_sepulsa_response("PDAM")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.create_pdam_bill_transaction(customer_number="1998900001",
                                                   product_id=87,
                                                   operator_code="pdam_aetra",
                                                   order_id=str(uuid.uuid4()))
    assert_create_transaction(response)


@patch("requests.request")
def test_inquire_mobile_postpaid(mock_request, assert_mobile_postpaid_details,
                                 generate_sepulsa_response):
    """ inquire mobile postpaid from sepulsa """
    response = generate_sepulsa_response("INQUIRE_MOBILE_POSTPAID")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.inquire_mobile_postpaid(
        customer_number="081234000001",
        product_id=113,
    )
    assert_mobile_postpaid_details(response)


@patch("requests.request")
def test_create_mobile_postpaid_transaction(mock_request,
                                            assert_create_transaction,
                                            generate_sepulsa_response):
    """ create mobile postpaid from sepulsa """
    response = generate_sepulsa_response("MOBILE_POSTPAID")
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = response

    client = build_client(BASE_URL, USERNAME, PASSWORD)
    response = client.create_mobile_postpaid_transaction(
        customer_number="081234000001",
        product_id=113,
        order_id=str(uuid.uuid4()))
    assert_create_transaction(response)
