from oy import build_client
from oy.exceptions import ProviderError


def test_build_client():
    client = build_client(
        "https://sandbox.oyindonesia.com/staging/partner", "myuser", "987654"
    )

    try:
        response = client.get_balance()
    except ProviderError as error:
        print(error.message, error.original_exception)
    else:
        print(response)

    try:
        response = client.inquiry_account("014", "1111111111")
    except ProviderError as error:
        print(error.message, error.original_exception)
    else:
        print(response)
