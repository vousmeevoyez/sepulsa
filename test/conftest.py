"""
    Fixtures
"""
from unittest.mock import Mock
import pytest
from test.sample import SEPULSA_RESPONSE


@pytest.fixture
def generate_sepulsa_response():

    def _generate_sepulsa_response(api_name):
        """ fixture to create sepulsa response based on api name"""
        return SEPULSA_RESPONSE[api_name]

    return _generate_sepulsa_response


@pytest.fixture
def setup_http_response():

    def _make_http_response(status_code, response=None, text=None):
        """ fixture to create http response """
        http_response = Mock(status_code=status_code)

        if response is not None:
            http_response.json.return_value = response

        if text is not None:
            http_response.json.side_effect = ValueError
            http_response.text = text

        return http_response

    return _make_http_response


@pytest.fixture
def setup_request():

    def _make_request(
        method="POST",
        url="https://sandbox.oyindonesia.com/staging/partner/api/inquiry",
        data={
            "recipient_bank": "014",
            "recipient_account": "1239812390"
        },
    ):
        mock_request = Mock()
        mock_request.to_representation.return_value = {
            "method": method,
            "url": url,
            "data": data,
        }
        return mock_request

    return _make_request


@pytest.fixture
def setup_response():

    def _make_response(response=None):
        mock_response = Mock()

        mock_response_payload = response
        if response is None:
            mock_response_payload = {
                "status": {
                    "code": "000",
                    "message": "Success"
                },
                "recipient_bank": "014",
                "recipient_account": "1239812390",
                "recipient_name": "John Doe",
                "timestamp": "16-10-2019 09:55:31",
            }

        mock_response.to_representation.return_value = mock_response_payload
        return mock_response

    return _make_response


"""
    reusable helper to help assert parameters
"""


@pytest.fixture
def assert_list():

    def _assert_list(response):
        """ reusable assert for list of data that returned from sepulsa """
        assert response["self"]
        assert response["first"]
        assert response["last"]
        assert response["list"]

    return _assert_list


@pytest.fixture
def assert_transaction_details():

    def _assert_transaction_details(response, data_details=None):
        """ reusable assert for transaction details from sepulsa """
        assert response["transaction_id"]
        assert response["type"]
        assert response["created"]
        assert response["changed"]
        assert response["customer_number"]
        assert response["order_id"]
        assert response["price"]
        assert response["status"]
        assert response["serial_number"]
        assert response["amount"]
        assert response["product_id"]
        assert response["product_id"]["product_id"]
        assert response["product_id"]["type"]
        assert response["product_id"]["label"]
        assert response["product_id"]["operator"]
        assert response["product_id"]["nominal"]
        assert response["product_id"]["price"]
        assert response["product_id"]["enabled"]

        # this field only exist for mobile payment / pulsa
        if "field_denom" in response["product_id"]:
            assert response["product_id"]["field_denom"]

        # this field only exist for pln
        if response["type"] == "electricity":
            assert response["meter_number"]
            assert response["token"]

        if "payment_period" in response:
            assert response["payment_period"]

        # there case where the data is not empty
        # to make sure data is like we expected
        # we define data details and validate it here
        if data_details is not None:
            for key in data_details:
                if response["data"][key] == "":
                    assert response["data"][key] == ""
                else:
                    assert response["data"][key]

    return _assert_transaction_details


@pytest.fixture
def assert_bpjs_kesehatan():

    def _assert_bpjs_kesehatan(response):
        assert response["trx_type"]
        assert response["product_type"]
        assert response["stan"]
        assert response["premi"]
        assert response["admin_charge"]
        assert response["amount"]
        assert response["datetime"]
        assert response["merchant_code"]
        assert response["rc"]
        assert response["no_va"]
        assert response["periode"]
        assert response["name"]
        assert response["kode_cabang"]
        assert response["nama_cabang"]
        assert response["sisa"]
        assert response["va_count"]
        assert response["no_va_kk"]
        assert response["trx_id"] == ""
        assert response["status"]

    return _assert_bpjs_kesehatan


@pytest.fixture
def assert_pbb_transaction_details():

    def _assert_pbb_transaction_details(response, data_details=None):
        """ reusable assert for pbb transaction details from sepulsa """
        assert response["changed"]
        assert response["transaction_id"]
        assert response["customer_id"]
        assert response["order_id"]
        assert response["amount"]
        assert response["price"]
        assert response["created"]
        assert response["product"]["code"]
        assert response["product"]["product_type"]
        assert response["product"]["label"]
        assert response["product"]["operator"]
        assert response["product"]["nominal"] == 0
        assert response["reference_no"]

        # there case where the data is not empty
        # to make sure data is like we expected
        # we define data details and validate it here
        if data_details is not None:
            for key in data_details:
                if response["data"][key] == "":
                    assert response["data"][key] == ""
                else:
                    assert response["data"][key]

    return _assert_pbb_transaction_details


@pytest.fixture
def assert_create_transaction():

    def _assert_create_transaction(response):
        assert response["transaction_id"]
        assert response["created"]
        assert response["changed"]
        assert response["customer_number"]
        assert response["order_id"]
        assert response["price"]
        assert response["status"]
        assert response["serial_number"] == ""
        assert response["amount"]
        assert response["product_id"]
        assert response["product_id"]["product_id"]
        assert response["product_id"]["type"]
        assert response["product_id"]["label"]
        assert response["product_id"]["operator"]
        assert response["product_id"]["nominal"]
        assert response["product_id"]["price"]
        assert response["product_id"]["enabled"]

        if "payment_period" in response:
            assert response["payment_period"]

        if "data" in response:
            assert response["data"] == ""

        if "operator_code" in response:
            assert response["operator_code"]

    return _assert_create_transaction


@pytest.fixture
def assert_create_pbb_transaction():

    def _assert_create_pbb_transaction(response):
        assert response["transaction_id"]
        assert response["customer_id"]
        assert response["order_id"]
        assert response["amount"]
        assert response["price"]
        assert response["created"]
        assert response["product"]["code"]
        assert response["product"]["product_type"]
        assert response["product"]["label"]
        assert response["product"]["operator"]
        assert response["product"]["nominal"] == 0
        assert response["reference_no"]

    return _assert_create_pbb_transaction


@pytest.fixture
def assert_create_pkb_transaction():

    def _assert_create_pkb_transaction(response):
        assert response["transaction_id"]
        assert response["customer_id"]
        assert response["order_id"]
        assert response["amount"]
        assert response["price"]
        assert response["created"]
        assert response["product"]["code"]
        assert response["product"]["product_type"]
        assert response["product"]["label"]
        assert response["product"]["operator"]
        assert response["product"]["nominal"] == 0
        assert response["reference_no"]

    return _assert_create_pkb_transaction


@pytest.fixture
def assert_pln_postpaid_bills():

    def _assert_pln_postpaid_bills(pln_bills):
        assert pln_bills[0]["bill_period"]

        if "produk" in pln_bills[0]:
            assert pln_bills[0]["produk"]

        assert pln_bills[0]["due_date"]
        assert pln_bills[0]["meter_read_date"]
        assert pln_bills[0]["total_electricity_bill"]
        assert pln_bills[0]["incentive"]
        assert pln_bills[0]["value_added_tax"]
        assert pln_bills[0]["penalty_fee"]
        assert pln_bills[0]["previous_meter_reading1"]
        assert pln_bills[0]["current_meter_reading1"]
        assert pln_bills[0]["previous_meter_reading2"]
        assert pln_bills[0]["current_meter_reading2"]
        assert pln_bills[0]["previous_meter_reading3"]
        assert pln_bills[0]["current_meter_reading3"]

    return _assert_pln_postpaid_bills


@pytest.fixture
def assert_pdam_bills():

    def _assert_pdam_bills(pdam_bills):
        assert pdam_bills[0]["bill_amount"]
        assert pdam_bills[0]["bill_date"]
        assert pdam_bills[0]["kubikasi"]
        assert pdam_bills[0]["penalty"]
        assert pdam_bills[0]["waterusage_bill"]
        assert pdam_bills[0]["total_fee"]
        assert pdam_bills[0]["detail_fee"]
        assert pdam_bills[0]["detail_fee"]["pdam_fee"]
        assert pdam_bills[0]["detail_fee"]["maintenance_fee"]
        assert pdam_bills[0]["detail_fee"]["wastewater_fee"]
        assert pdam_bills[0]["detail_fee"]["service_fee"]
        assert pdam_bills[0]["detail_fee"]["stamp_fee"]
        assert pdam_bills[0]["detail_fee"]["reconnection_fee"]
        assert pdam_bills[0]["detail_fee"]["nonwater_fee"]
        assert pdam_bills[0]["detail_fee"]["installment_amount"]
        assert pdam_bills[0]["detail_fee"]["seal_penalty"]
        assert pdam_bills[0]["detail_fee"]["lltt_fee"]
        assert pdam_bills[0]["detail_fee"]["gwt"]
        assert pdam_bills[0]["detail_fee"]["vat"]
        assert pdam_bills[0]["lift_usage"]
        assert pdam_bills[0]["total_usage"]
        assert pdam_bills[0]["detail_usage"]["usage1"]
        assert pdam_bills[0]["detail_usage"]["usage2"]
        assert pdam_bills[0]["detail_usage"]["usage3"]
        assert pdam_bills[0]["detail_usage"]["usage4"] == ""
        assert pdam_bills[0]["info_text"]

    return _assert_pdam_bills


@pytest.fixture
def assert_multifinance_details():

    def _assert_multifinance_details(response):
        assert response["product_code"]
        assert response["time"]
        assert response["id_pelanggan1"]
        assert response["id_pelanggan2"] == ""
        assert response["id_pelanggan3"] == ""
        assert response["nominal"]
        assert response["admin_fee"]
        assert response["ref_1"]
        assert response["ref_2"]
        assert response["ref_3"] == ""

        if response["status"] == "00":
            assert response["status"] == "00"
        else:
            assert response["status"] is True

        assert response["note"]
        assert response["customer_name"]
        assert response["bill_ref_number"]
        assert response["pt_name"]
        assert response["cardnumber"]
        assert response["tenor"]
        assert response["last_paid_periode"]
        assert response["last_paid_duedate"]
        assert response["od_pinalty_fee"]
        assert response["misc_fee"]
        assert response["jumlah_tagihan"]
        assert response["terbilang"]

    return _assert_multifinance_details


@pytest.fixture
def assert_tv_bill_details():

    def _assert_tv_bill_details(response):
        assert response["stan"]
        assert response["reference_no"]
        assert response["customer_id"]
        assert response["customer_name"]
        assert response["bill_count"]
        assert response["bill_period"]
        assert response["bill_amount"]
        assert response["admin_fee"]
        assert response["total_amount"]
        assert response["message"]

    return _assert_tv_bill_details


@pytest.fixture
def assert_mobile_postpaid_details():

    def _assert_mobile_postpaid_details(response):
        assert response["reference_no"]
        assert response["customer_no"]
        assert response["customer_name"]
        assert response["bill_count"]
        assert response["bill_periode"]
        assert response["bill_amount"]
        assert response["admin_fee"]
        assert response["total_amount"]

    return _assert_mobile_postpaid_details


@pytest.fixture
def assert_tv_prepaid_details():

    def _assert_tv_prepaid_details(response):
        assert response["stan"]
        assert response["reference_no"]
        assert response["customer_name"]
        assert response["total_price"]

        if "customer_number" in response:
            assert response["customer_number"]

        if "message" in response:
            assert response["message"]

        if "status" in response:
            assert response["status"] is True

        if "trx_id" in response:
            assert response["trx_id"]

    return _assert_tv_prepaid_details


@pytest.fixture
def assert_education_details():

    def _assert_education_details(response):
        assert response[0]["bill_date"]
        assert response[0]["bill_label"]
        assert response[0]["bill_item_id"]
        assert response[0]["bill_amount"]
        assert response[0]["penalty_fee"]
        assert response[0]["due_datetime"]
        assert response[0]["expired_datetime"]

    return _assert_education_details


@pytest.fixture
def assert_pbb_details():

    def _assert_pbb_details(response):
        assert response["customer_name"]
        assert response["payment_period"]
        assert response["kecamatan"]
        assert response["kelurahan"]
        assert response["surface_area"]
        assert response["building_area"]
        assert response["due_date"]
        assert response["bill_amount"]
        assert response["admin_charge"]
        assert response["total_amount"]
        assert response["reference_no"]
        assert response["bill_items"]

    return _assert_pbb_details


@pytest.fixture
def assert_pkb_details():

    def _assert_pkb_details(response):
        assert response["customer"]["name"]
        assert response["customer"]["identity_number"]
        assert response["customer"]["address"]
        assert response["customer"]["last_date_previous_tax"]
        assert response["customer"]["last_date_new_tax"]
        assert response["vehicle"]["identity_number"]
        assert response["vehicle"]["engine_number"]
        assert response["vehicle"]["registration_number"]
        assert response["vehicle"]["license_plate_color"]
        assert response["vehicle"]["ownership"]
        assert response["vehicle"]["category"]
        assert response["vehicle"]["brand"]
        assert response["vehicle"]["model"]
        assert response["vehicle"]["manufacture_year"]
        assert response["bill_amount"]
        assert response["admin_charge"]
        assert response["bill"]["bbn_amount"]
        assert response["bill"]["bbn_penalty_fee"]
        assert response["bill"]["pkb_amount"]
        assert response["bill"]["pkb_penalty_fee"]
        assert response["bill"]["swd_amount"]
        assert response["bill"]["swd_penalty_fee"]
        assert response["bill"]["stnk_admin_charge"]
        assert response["bill"]["tnkb_admin_charge"]
        assert response["bill"]["total_penalty_fee"]
        assert response["bill"]["total_amount"]
        assert response["info_text"] == ""
        assert response["reference_no"]

    return _assert_pkb_details


@pytest.fixture
def assert_inquire_pln_prepaid():

    def _assert_inquire_pln_prepaid(response):
        assert response["admin_charge"] == 0
        assert response["trx_id"] == ""
        assert response["stan"]
        assert response["datetime"]
        assert response["merchant_code"]
        assert response["bank_code"]
        assert response["terminal_id"]
        assert response["material_number"]
        assert response["subscriber_id"]
        assert response["pln_refno"]
        assert response["switcher_refno"]
        assert response["subscriber_name"]
        assert response["subscriber_segmentation"]
        assert response["power"]
        assert response["distribution_code"]
        assert response["service_unit"]
        assert response["service_unit_phone"]
        assert response["total_repeat"]
        assert response["status"]
        assert response["max_kwh_unit"]
        assert response["power_purchase_unsold"]
        assert response["power_purchase_unsold2"]

    return _assert_inquire_pln_prepaid

@pytest.fixture
def assert_inquire_pln_postpaid():
    def _assert_inquire_pln_postpaid(response):
        assert response["amount"] == "136856"
        assert response["admin_charge"] == "1600"
        assert response["trx_id"] == ""
        assert response["stan"]
        assert response["datetime"]
        assert response["merchant_code"]
        assert response["bank_code"]
        assert response["rc"]
        assert response["terminal_id"]
        assert response["material_number"] == ""
        assert response["subscriber_id"]
        assert response["subscriber_name"]
        assert response["switcher_refno"]
        assert response["subscriber_segmentation"]
        assert response["power"]
        assert response["outstanding_bill"]
        assert response["bill_status"]
        assert response["blth_summary"]
        assert response["stand_meter_summary"]
        assert response["bills"]

    return _assert_inquire_pln_postpaid
