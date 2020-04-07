"""
    Example how to use Oy-Client
"""
from oy import build_client

# initialize client
base_url = "https://sandbox.oyindonesia.com/staging/partner"
CLIENT = build_client(base_url, "username", "password")

# get bank account information
response = CLIENT.inquiry_account("014", "4740625654")
print(response)

# Send money to bank account
base_url = "https://sandbox.oyindonesia.com/staging/partner"
recipient_bank = "009"
recipient_account = "1122334455"
amount = 10000
partner_trx_id = "some-unique-id"

response = CLIENT.disburse(recipient_bank, recipient_account, amount, partner_trx_id)
print(response)

# get disbursement status
reference_id = "some-reference-id"
response = CLIENT.disburse_status(reference_id)
print(response)

# get master balance
response = CLIENT.get_balance()
print(response)

# geneerate virtual account
response = CLIENT.generate_va("002", 10000, "some-unqiue-id2")
print(response)

# generate list of generated virtual account
response = CLIENT.get_list_of_va()
print(response)

# get virtual account details
response = CLIENT.get_va_info("some-va-id")
print(response)
