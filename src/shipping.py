import requests as requests


def calculate_shipping(country, order_total):
    url = (
        "https://npovmrfcyzu2gu42pmqa7zce6a0zikbf.lambda-url.eu-west-2.on.aws/?country="
        + country
    )

    response = requests.get(url)
    response.raise_for_status()

    region = response.json()["region"]

    shipping = 0.0

    if region == "UK":
        if order_total < 100.0:
            shipping = 4.99

    if region == "EU":
        if order_total < 100:
            shipping = 8.99
        else:
            shipping = 4.99

    if region == "OTHER":
        shipping = 9.99

    return shipping
