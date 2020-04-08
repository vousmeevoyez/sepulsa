"""
    sepulsa python client examples
"""
import uuid
from sepulsa import build_client

USERNAME = "sepulsausername"
PASSWORD = "sepulsapassword"
BASE_URL = "https://horven-api.sumpahpalapa.com/api"

CLIENT = build_client(BASE_URL, USERNAME, PASSWORD)
""" get real all products data from sepulsa """
response = CLIENT.get_products()
""" get create mobile prepaid from sepulsa """
response = CLIENT.create_mobile_prepaid_transaction(
    customer_number="081234567890", product_id=99, order_id=str(uuid.uuid4())
)
""" inquire bpjs kesehatan from sepulsa """
response = CLIENT.inquire_bpjs_kesehatan(
    customer_number="0000001430071801", product_id=34, payment_period="01"
)
""" get create bpjs kesehatan from sepulsa """
response = CLIENT.create_bpjs_kesehatan_transaction(
    customer_number="0000001430071801",
    product_id=34,
    payment_period="01",
    order_id=str(uuid.uuid4()),
)
""" get inquire pln prepaid from sepulsa """
response = CLIENT.inquire_pln_prepaid(customer_number="01428800700", product_id=25)
""" create pln prepaid transaction from sepulsa """
response = CLIENT.create_pln_prepaid_transaction(
    customer_number="08123456789",
    pln_meter_no="01428800700",
    product_id=25,
    order_id=str(uuid.uuid4()),
)
""" inquire pln postpaid from sepulsa """
response = CLIENT.inquire_pln_postpaid(customer_number="512345610000", product_id=80)
""" create pln postpaid from sepulsa """
response = CLIENT.create_pln_postpaid_transaction(
    customer_number="512345610000", product_id=80, order_id=str(uuid.uuid4())
)
""" inquire telkom bill from sepulsa """
response = CLIENT.inquire_telkom_bill(customer_number="0218800007", product_id=82)
""" create telkom bill transaction from sepulsa """
response = CLIENT.create_telkom_bill_transaction(
    customer_number="0218800007", product_id=82, order_id=str(uuid.uuid4())
)
""" get all pdam operators from sepulsa """
response = CLIENT.get_pdam_operators(product_id=87)
""" inquire pdam bills from sepulsa """
response = CLIENT.inquire_pdam_bill(
    customer_number="1998900001", product_id=87, operator_code="pdam_aetra"
)
""" create pdam bill transaction from sepulsa """
response = CLIENT.create_pdam_bill_transaction(
    customer_number="1998900001",
    product_id=87,
    operator_code="pdam_aetra",
    order_id=str(uuid.uuid4()),
)
""" inquire mobile postpaid from sepulsa """
response = CLIENT.inquire_mobile_postpaid(
    customer_number="081234000001", product_id=113
)
""" create mobile postpaid from sepulsa """
response = CLIENT.create_mobile_postpaid_transaction(
    customer_number="081234000001", product_id=113, order_id=str(uuid.uuid4())
)
