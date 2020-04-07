"""
    Test all possible response from sepulsa to our response class
"""
from json import JSONDecodeError
from unittest.mock import patch

import pytest

from sepulsa.response import SepulsaResponse
from sepulsa.core.exceptions import ResponseError


def check_response(mock_http_response, expected_exception):
    http_request = SepulsaResponse()
    http_request.set(mock_http_response)
    # make sure response doesnt contain status
    with pytest.raises(expected_exception):
        http_request.to_representation()


def check_responses(mock_http_responses, expected_exception):
    for mock_http_response in mock_http_responses:
        check_response(mock_http_response, expected_exception)


def test_response_plain(setup_http_response):
    """ simulate error response from sepulsa server as plain text """
    plain_response = "plain text"
    mock_http_response = setup_http_response(403, text=plain_response)

    check_response(mock_http_response, ResponseError)


def test_mobile_trx_details_response(setup_http_response):
    """ simulate error response from get mobile transaction details from
    sepulsa server"""

    sepulsa_response = {
        "transaction_id": "79325",
        "type": "mobile",
        "created": "1586154720",
        "changed": "1586154720",
        "customer_number": "081234000011",
        "product_id": {
            "product_id": "9",
            "type": "mobile",
            "label": "Telkomsel Rp 50,000",
            "operator": "telkomsel",
            "nominal": "50000",
            "price": 50000,
            "enabled": "1",
            "field_denom": "50000.00",
            "field_paket_data": False,
        },
        "order_id": "9bcc3b8a-1322-43b6-b1e9-ca4b928fafcd",
        "price": "50000",
        "status": "failed",
        "response_code": "99",
        "serial_number": None,
        "amount": "50000",
        "token": None,
        "data": {"message": "General Error"},
    }
    mock_http_response = setup_http_response(200, sepulsa_response)

    check_response(mock_http_response, ResponseError)


def test_inquiry_bpjs_kesehatan_response(setup_http_response):
    """ simulate error response inquiry bpjs kesehatan from
    sepulsa server"""
    mock_http_responses = []

    sepulsa_response = {
        "trx_id": "",
        "rc": "0014",
        "status": False,
        "response_code": "20",
        "desc": "NOMOR VIRTUAL ACCOUNT SALAH, MOHON TELITI KEMBALI",
        "message": "Nomor virtual account salah, mohon teliti kembali",
    }
    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "status": False,
        "response_code": "20",
        "message": "Wrong Number / Number Blocked / Number Expired",
        "rc": "20",
        "trx_id": "",
        "desc": "Failed",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    check_responses(mock_http_responses, ResponseError)


def test_inquiry_pln_prepaid_response(setup_http_response):
    """ simulate error response inquiry pln prepaid from
    sepulsa server"""
    mock_http_responses = []

    sepulsa_response = {
        "status": False,
        "message": "Error-cut-off is in progress",
        "response_code": "24",
    }
    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "status": False,
        "response_code": "23",
        "message": "Connection Timeout",
        "rc": "23",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "status": False,
        "response_code": "20",
        "message": "IDPEL YANG ANDA MASUKKAN SALAH, MOHON TELITI KEMBALI",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    check_responses(mock_http_responses, ResponseError)


def test_inquiry_pln_postpaid_response(setup_http_response):
    """ simulate error response inquiry pln postpaid from
    sepulsa server"""
    mock_http_responses = []

    sepulsa_response = {
        "trx_id": "",
        "rc": "0088",
        "status": False,
        "response_code": "50",
        "message": "Tagihan sudah terbayar",
    }
    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "trx_id": "",
        "rc": "0014",
        "status": False,
        "response_code": "20",
        "message": "NOMOR METER/IDPEL YANG ANDA MASUKKAN SALAH, MOHON TELITI KEMBALI.",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "response_code": "23",
        "status": False,
        "message": "Request timed out",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    check_responses(mock_http_responses, ResponseError)


def test_inquiry_telkom_response(setup_http_response):
    """ simulate error response inquiry telkom from
    sepulsa server"""
    mock_http_responses = []

    sepulsa_response = {
        "trx_id": "",
        "rc": "0005",
        "desc": "EXT: NOMOR TELEPON/IDPEL TIDAK TERDAFTAR",
        "status": False,
        "response_code": "20",
        "message": "Ext: nomor telepon/idpel tidak terdaftar",
    }
    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "trx_id": "",
        "rc": "0005",
        "desc": "EXT: NOMOR TELEPON/IDPEL TIDAK TERDAFTAR",
        "status": False,
        "response_code": "20",
        "message": "Ext: nomor telepon/idpel tidak terdaftar",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "trx_id": "",
        "rc": "0005",
        "desc": "Gagal, tagihan sudah terbayar",
        "status": False,
        "response_code": "99",
        "message": "Gagal, tagihan sudah terbayar",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "response_code": "23",
        "status": False,
        "message": "Request timed out",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "rc": "0005",
        "desc": "EXT: TRANSAKSI DITOLAK KARENA NOMOR TELEPON YANG DIMAKSUD TELAH MELAMPAUI BATAS MAKSIMUM JUMLAH BILL (MAX. 3)",
        "status": False,
        "response_code": "99",
        "message": "Ext: transaksi ditolak karena nomor telepon yang dimaksud telah melampaui batas maksimum jumlah bill (max. 3)",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    check_responses(mock_http_responses, ResponseError)


def test_inquiry_pdam_response(setup_http_response):
    """ simulate error response inquiry pdam from
    sepulsa server"""
    mock_http_responses = []

    sepulsa_response = {
        "trx_id": "",
        "rc": "14",
        "status": False,
        "desc": "No Pelanggan salah, silahkan teliti kembali",
        "response_code": "20",
        "message": "No pelanggan salah, silahkan teliti kembali",
    }
    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "trx_id": "",
        "rc": "34",
        "status": False,
        "desc": "Tagihan sudah terbayar",
        "response_code": "50",
        "message": "Tagihan sudah terbayar",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "response_code": "23",
        "status": False,
        "message": "Request timed out",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    check_responses(mock_http_responses, ResponseError)


def test_inquiry_mobile_postpaid_response(setup_http_response):
    """ simulate error response inquiry pdam from
    sepulsa server"""
    mock_http_responses = []

    sepulsa_response = {
        "response_code": "20",
        "message": "Id pelanggan tidak ditemukan",
    }
    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {"response_code": "99", "message": "Inquiry gagal"}

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    sepulsa_response = {
        "response_code": "23",
        "message": "Host atau biller sedang offline",
    }

    mock_http_response = setup_http_response(200, sepulsa_response)
    mock_http_responses.append(mock_http_response)

    check_responses(mock_http_responses, ResponseError)
