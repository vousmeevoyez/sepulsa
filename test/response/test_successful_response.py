"""
    Test all possible success response from sepulsa to our response class
"""
import pytest
from sepulsa.response import SepulsaResponse
from sepulsa.core.exceptions import ResponseError


def check_response(mock_http_response):
    http_request = SepulsaResponse()
    http_request.set(mock_http_response)
    # make sure response doesnt contain status
    response = http_request.to_representation()
    return response


'''
def test_get_product_list_response(setup_http_response,
                                   generate_sepulsa_response, assert_list):
    """ simulate success get product list response from sepulsa """
    sepulsa_response = generate_sepulsa_response("PRODUCTS")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_list(response)
'''


def test_get_balance_response(setup_http_response, generate_sepulsa_response):
    """ simulate success get balance response from sepulsa """

    sepulsa_response = generate_sepulsa_response("BALANCE")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert response["balance"]


def test_get_transaction_history_response(setup_http_response,
                                          generate_sepulsa_response,
                                          assert_list):
    """ simulate success get transaction history response from sepulsa """

    sepulsa_response = generate_sepulsa_response("TRANSACTIONS")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_list(response)


def test_get_transaction_details_response(setup_http_response,
                                          generate_sepulsa_response,
                                          assert_transaction_details):
    """ simulate success get transaction details response from sepulsa """

    sepulsa_response = generate_sepulsa_response("TRANSACTION_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)


def test_get_xl_profile_subscriber_response(setup_http_response,
                                            generate_sepulsa_response):
    """ simulate success get profile subscriber response from sepulsa """
    sepulsa_response = generate_sepulsa_response("XL_SUBSCRIBER")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert response["code"]
    assert response["payment_category"]
    assert response["customer_type"]
    assert response["end_cycle_date"]


def test_inquire_bpjs_kesehatan_response(setup_http_response,
                                         generate_sepulsa_response,
                                         assert_bpjs_kesehatan):
    """ simulate success inquire bpjs kesehatan response from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_BPJS_KESEHATAN")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_bpjs_kesehatan(response)


def test_create_bpjs_kesehatan_trx_response(setup_http_response,
                                            generate_sepulsa_response,
                                            assert_create_transaction):
    """ simulate success creating bpjs kesehatan response from sepulsa """
    sepulsa_response = generate_sepulsa_response("BPJS_KESEHATAN")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_bpjs_kesehatan_details_response(setup_http_response,
                                         generate_sepulsa_response,
                                         assert_transaction_details):
    """ simulate success bpjs kesehatan details response from sepulsa """

    sepulsa_response = generate_sepulsa_response("BPJS_KESEHATAN_DETAIL")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)

    data_details = [
        "trx_type",
        "product_type",
        "stan",
        "premi",
        "admin_charge",
        "amount",
        "datetime",
        "merchant_code",
        "rc",
        "no_va",
        "periode",
        "name",
        "kode_cabang",
        "nama_cabang",
        "sisa",
        "va_count",
        "no_va_kk",
        "trx_id",
        "info_text",
        "sw_reff",
        "waktu_lunas",
        "kode_loket",
        "nama_loket",
        "alamat_loket",
        "phone_loket",
        "kode_kab_kota",
    ]

    assert_transaction_details(response, data_details)


def test_inquire_pln_prepaid_response(setup_http_response,
                                      generate_sepulsa_response,
                                      assert_inquire_pln_prepaid):
    """ simulate success inquire pln prepaid response from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_PLN_PREPAID")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_inquire_pln_prepaid(response)


def test_pln_prepaid_response(setup_http_response, assert_create_transaction,
                              generate_sepulsa_response):
    """ simulate success create pln prepaid response from sepulsa """

    sepulsa_response = generate_sepulsa_response("PLN_PREPAID")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_pln_prepaid_details_response(setup_http_response,
                                      generate_sepulsa_response,
                                      assert_transaction_details):
    """ simulate success pln details response from sepulsa """

    sepulsa_response = generate_sepulsa_response("PLN_PREPAID_DETAIL")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)

    data_details = [
        "admin_charge",
        "trx_id",
        "stan",
        "datetime",
        "merchant_code",
        "bank_code",
        "terminal_id",
        "material_number",
        "subscriber_id",
        "pln_refno",
        "switcher_refno",
        "subscriber_name",
        "subscriber_segmentation",
        "power",
        "distribution_code",
        "service_unit",
        "service_unit_phone",
        "total_repeat",
        "rc",
        "angsuran",
        "info_text",
        "jml_kwh",
        "max_kwh",
        "meterai",
        "power_purchase",
        "ppj",
        "ppn",
        "produk",
        "settlement",
        "token",
        "vending_refno",
    ]

    assert_transaction_details(response, data_details)


def test_inquire_pln_postpaid_response(setup_http_response,
                                       generate_sepulsa_response,
                                       assert_inquire_pln_postpaid,
                                       assert_pln_postpaid_bills):
    """ simulate success inquire pln postpaid response from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_PLN_POSTPAID")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)

    assert_inquire_pln_postpaid(response)
    assert_pln_postpaid_bills(response["bills"])


def test_pln_postpaid_details_response(setup_http_response,
                                       generate_sepulsa_response,
                                       assert_transaction_details,
                                       assert_pln_postpaid_bills):
    """ simulate success pln postpaid details response from sepulsa """

    sepulsa_response = generate_sepulsa_response("PLN_POSTPAID_DETAIL")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    data_details = [
        "amount",
        "admin_charge",
        "trx_id",
        "stan",
        "datetime",
        "merchant_code",
        "bank_code",
        "rc",
        "terminal_id",
        "material_number",
        "subscriber_id",
        "subscriber_name",
        "switcher_refno",
        "subscriber_segmentation",
        "power",
        "outstanding_bill",
        "bill_status",
        "blth_summary",
        "stand_meter_summary",
        "payment_status",
        "payment_date",
        "payment_time",
        "pln_refno",
        "service_unit",
        "service_unit_phone",
        "info_text",
        "bills",
    ]
    assert_transaction_details(response, data_details)
    assert_pln_postpaid_bills(response["data"]["bills"])


def test_inquire_telkom_response(setup_http_response, generate_sepulsa_response,
                                 assert_inquire_telkom_bill):
    """ simulate success inquire telkom response from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_TELKOM")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_inquire_telkom_bill(response)


def test_create_telkom_trx_response(setup_http_response,
                                    generate_sepulsa_response,
                                    assert_create_transaction):
    """ simulate success create telkom trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("TELKOM")

    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_telkom_details_response(setup_http_response, generate_sepulsa_response,
                                 assert_transaction_details):
    """ simulate success get telkom trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("TELKOM_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    data_details = [
        "trx_id",
        "stan",
        "datetime",
        "code",
        "rc",
        "product_type",
        "produk",
        "request_type",
        "id_pelanggan",
        "nama_pelanggan",
        "no_reference",
        "bulan_thn",
        "jumlah_tagihan",
        "jumlah_adm",
        "jumlah_bayar",
        "description",
        "status",
    ]
    assert_transaction_details(response, data_details)


def test_pdam_operators(setup_http_response, generate_sepulsa_response,
                        assert_pdam_operators):
    """ simulate success get pdam operators from sepulsa """

    sepulsa_response = generate_sepulsa_response("PDAM_OPERATOR")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_pdam_operators(response)


def test_inquire_pdam_response(setup_http_response, generate_sepulsa_response,
                               assert_pdam_bills, assert_inquire_pdam):
    """ simulate success get inquire pdam from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_PDAM")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_inquire_pdam(response)
    assert_pdam_bills(response["bills"])


def test_create_pdam_trx_response(setup_http_response,
                                  generate_sepulsa_response,
                                  assert_create_transaction):
    """ simulate success create pdam trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("PDAM")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_pdam_details_response(setup_http_response, generate_sepulsa_response,
                               assert_transaction_details, assert_pdam_bills):
    """ simulate success pdam trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("PDAM_DETAIL")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    data_details = [
        "trx_id",
        "stan",
        "amount",
        "merchant_code",
        "rc",
        "admin_charge",
        "local_trx_time",
        "local_trx_date",
        "settlement_date",
        "acquiring_institution_id",
        "retrieval_ref_no",
        "idpel",
        "blth",
        "name",
        "customer_address",
        "group_code",
        "group_desc",
        "bill_count",
        "bill_repeat_count",
        "rp_tag",
        "bills",
    ]

    assert_transaction_details(response, data_details)
    assert_pdam_bills(response["data"]["bills"])

    assert response["data"]["biller_ref"]
    assert response["data"]["switching_ref"]
    assert response["data"]["datetime"]
    assert response["data"]["waktu_lunas"]


def test_inquire_multifinance_response(setup_http_response,
                                       generate_sepulsa_response,
                                       assert_multifinance_details):
    """ simulate success inquire multifnance from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_MULTIFINANCE")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_multifinance_details(response)


def test_create_multifinance_trx_response(setup_http_response,
                                          generate_sepulsa_response,
                                          assert_create_transaction):
    """ simulate success create multifnance trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("MULTIFINANCE")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_multifinance_details_response(setup_http_response,
                                       generate_sepulsa_response,
                                       assert_transaction_details,
                                       assert_multifinance_details):
    """ simulate success get multifnance details from sepulsa """

    sepulsa_response = generate_sepulsa_response("MULTIFINANCE_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)
    assert_multifinance_details(response["data"])


def test_create_game_voucher_trx_response(setup_http_response,
                                          generate_sepulsa_response,
                                          assert_create_transaction):
    """ simulate success create game voucher trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("GAME")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_game_voucher_details_response(setup_http_response,
                                       generate_sepulsa_response,
                                       assert_transaction_details):
    """ simulate success get game voucher trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("GAME_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)
    assert response["data"]["trx_id"]
    assert response["data"]["stan"]
    assert response["data"]["msisdn"]
    assert response["data"]["product_type"]
    assert response["data"]["rc"]
    assert response["data"]["management_code"]
    assert response["data"]["voucher_code"]
    assert response["data"]["serial_number"]
    assert response["data"]["voucher_password"]
    assert response["data"]["pin"]
    assert response["data"]["produk"]
    assert response["data"]["nominal"]
    assert response["data"]["desc"]


def test_inquire_tv_bill_responose(setup_http_response,
                                   generate_sepulsa_response,
                                   assert_tv_bill_details):
    """ simulate success inquire tv bill from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_TV_BILL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_tv_bill_details(response)


def test_create_tv_bill_trx_response(setup_http_response,
                                     generate_sepulsa_response,
                                     assert_create_transaction):
    """ simulate success create tv bill trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("TV_BILL")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_tv_bill_details_response(setup_http_response,
                                  generate_sepulsa_response,
                                  assert_transaction_details,
                                  assert_tv_bill_details):
    """ simulate success tv bill trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("TV_BILL_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)
    assert_tv_bill_details(response["data"])


def test_inquire_mobile_postpaid_response(setup_http_response,
                                          generate_sepulsa_response,
                                          assert_mobile_postpaid_details):
    """ simulate success inquire mobile postpaid from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_MOBILE_POSTPAID")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_mobile_postpaid_details(response)


def test_create_mobile_postpaid_trx_response(setup_http_response,
                                             generate_sepulsa_response,
                                             assert_create_transaction):
    """ simulate success create mobile postpaid trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("MOBILE_POSTPAID")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_mobile_trx_details_response(setup_http_response,
                                     generate_sepulsa_response,
                                     assert_transaction_details,
                                     assert_mobile_postpaid_details):
    """ simulate success getting mobile trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("MOBILE_POSTPAID_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)
    assert_mobile_postpaid_details(response["data"])


def test_create_ewallet_trx_response(setup_http_response,
                                     generate_sepulsa_response,
                                     assert_create_transaction):
    """ simulate success create e-wallet trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("EWALLET")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_ewallet_details_response(setup_http_response,
                                  generate_sepulsa_response,
                                  assert_transaction_details):
    """ simulate success getting ewallet trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("EWALLET_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)


def test_create_donation_response(setup_http_response,
                                  generate_sepulsa_response,
                                  assert_create_transaction):
    """ simulate success creating donation trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("DONATION")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_donation_details_response(setup_http_response,
                                   generate_sepulsa_response,
                                   assert_transaction_details):
    """ simulate success getting donation trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("DONATION_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)
    assert response["data"]["customer_name"]
    assert response["data"]["email"]
    assert response["data"]["amount"]
    assert response["data"]["reference_no"]
    assert response["data"]["datetime"]
    assert response["data"]["institution"]
    assert response["data"]["account_number"]


def test_inquire_bill_response(setup_http_response, generate_sepulsa_response):
    """ simulate success inquire bill from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_BILL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert response["reference_no"]
    assert response["bill_amount"]
    assert response["admin_fee"]
    assert response["total_amount"]
    assert response["other"] == {}
    assert response["customer_number"]


def test_create_bill_trx_response(setup_http_response,
                                  generate_sepulsa_response,
                                  assert_create_transaction):
    """ simulate success creating bill trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("BILL")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_bill_details_response(setup_http_response, generate_sepulsa_response,
                               assert_transaction_details):
    """ simulate success getting bill trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("BILL_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)


def test_inquire_tv_prepaid_response(setup_http_response,
                                     generate_sepulsa_response,
                                     assert_tv_prepaid_details):
    """ simulate success inquire tv prepaid from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_TV_PREPAID")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_tv_prepaid_details(response)


def test_create_tv_prepaid_trx_response(setup_http_response,
                                        generate_sepulsa_response,
                                        assert_create_transaction):
    """ simulate success create tv prepaid from sepulsa """

    sepulsa_response = generate_sepulsa_response("TV_PREPAID")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_tv_prepaid_details_response(setup_http_response,
                                     generate_sepulsa_response,
                                     assert_transaction_details,
                                     assert_tv_prepaid_details):
    """ simulate success get tv prepaid details from sepulsa """

    sepulsa_response = generate_sepulsa_response("TV_PREPAID_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)
    assert_tv_prepaid_details(response["data"])


def test_create_voucher_trx_response(setup_http_response,
                                     generate_sepulsa_response,
                                     assert_create_transaction):
    """ simulate success create voucher trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("VOUCHER")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_voucher_details_response(setup_http_response,
                                  generate_sepulsa_response,
                                  assert_transaction_details):
    """ simulate success get voucher trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("VOUCHER_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)
    assert response["data"]["trx_id"]
    assert response["data"]["stan"]
    assert response["data"]["msisdn"]
    assert response["data"]["product_type"]
    assert response["data"]["rc"]
    assert response["data"]["management_code"]
    assert response["data"]["voucher_code"]
    assert response["data"]["serial_number"]
    assert response["data"]["voucher_password"]
    assert response["data"]["pin"]
    assert response["data"]["produk"]
    assert response["data"]["nominal"]
    assert response["data"]["desc"] == ""


def test_education_inquire_response(setup_http_response,
                                    generate_sepulsa_response,
                                    assert_education_details):
    """ simulate success inquire education  from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_EDUCATION")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert response["reference_no"]
    assert response["customer_name"]
    assert response["bill_amount"]
    assert response["bill_count"]
    assert response["admin_fee"]
    assert_education_details(response["bills"])


def test_create_education_trx_response(setup_http_response,
                                       generate_sepulsa_response,
                                       assert_create_transaction):
    """ simulate success create education trxfrom sepulsa """

    sepulsa_response = generate_sepulsa_response("EDUCATION")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_education_details_response(setup_http_response,
                                    generate_sepulsa_response,
                                    assert_transaction_details,
                                    assert_education_details):
    """ simulate success get e education trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("EDUCATION_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_transaction_details(response)
    assert_education_details(response["data"]["bills"])


def test_inquire_pbb_response(setup_http_response, generate_sepulsa_response,
                              assert_pbb_details):
    """ simulate success inquire  pbb from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_PBB")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert response["product"]
    assert response["product"]["code"]
    assert response["product"]["product_type"]
    assert response["product"]["label"]
    assert response["product"]["operator"]
    assert response["product"]["nominal"] == 0
    assert response["customer_id"]
    assert response["reference_no"]
    assert response["amount"]
    assert response["price"]
    assert_pbb_details(response["data"])


def test_create_pbb_trx_response(setup_http_response, generate_sepulsa_response,
                                 assert_create_pbb_transaction):
    """ simulate success create  pbb trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("PBB")
    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_pbb_transaction(response)


def test_pbb_details_response(setup_http_response, generate_sepulsa_response,
                              assert_pbb_transaction_details,
                              assert_pbb_details):
    """ simulate success get pbb trx details  from sepulsa """

    sepulsa_response = generate_sepulsa_response("PBB_DETAIL")
    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_pbb_transaction_details(response)
    assert_pbb_details(response["data"])


def test_inquire_credit_card_response(setup_http_response,
                                      generate_sepulsa_response):
    """ simulate success nquiry credit card from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_CREDIT_CARD")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert response["reference_no"]
    assert response["customer_name"]
    assert response["customer_number"]
    assert response["status"]
    assert response["trx_id"] == ""


def test_create_credit_card_trx_response(setup_http_response,
                                         generate_sepulsa_response,
                                         assert_create_transaction):
    """ simulate success create credit card trx from sepulsa """

    sepulsa_response = generate_sepulsa_response("CREDIT_CARD")

    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_transaction(response)


def test_credit_card_details_response(setup_http_response,
                                      generate_sepulsa_response,
                                      assert_transaction_details):
    """ simulate success get credit card trx details from sepulsa """

    sepulsa_response = generate_sepulsa_response("CREDIT_CARD_DETAIL")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    data_details = [
        "reference_no",
        "customer_name",
        "bill_amount",
        "admin_fee",
        "total_amount",
    ]
    assert_transaction_details(response, data_details)


def test_inquire_pkb_response(setup_http_response, generate_sepulsa_response,
                              assert_pkb_details):
    """ simulate success inquire pkb from sepulsa """

    sepulsa_response = generate_sepulsa_response("INQUIRE_PKB")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert response["customer_id"]
    assert response["reference_no"]
    assert response["amount"]
    assert response["price"]
    assert response["product"]["code"]
    assert response["product"]["label"]
    assert response["product"]["product_type"]
    assert response["product"]["operator"]
    assert response["product"]["nominal"] == 0
    assert_pkb_details(response["data"])


def test_create_pkb_trx_response(setup_http_response, generate_sepulsa_response,
                                 assert_create_pbb_transaction):
    """ simulate success crete pkb transaction from sepulsa """

    sepulsa_response = generate_sepulsa_response("PKB")

    mock_http_response = setup_http_response(201, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_pbb_transaction(response)


def test_pkb_trx_details_response(setup_http_response,
                                  generate_sepulsa_response,
                                  assert_create_pkb_transaction,
                                  assert_pkb_details):
    """ simulate success get pkb transaction details from sepulsa """

    sepulsa_response = generate_sepulsa_response("PKB_DETAIL")

    mock_http_response = setup_http_response(200, sepulsa_response)

    response = check_response(mock_http_response)
    assert_create_pkb_transaction(response)
    assert_pkb_details(response["data"])
