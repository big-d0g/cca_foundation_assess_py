import pytest

from src.shipping import calculate_shipping
from src.countries import Country


@pytest.mark.parametrize(
    "country, order_total, shipping_cost",
    [
        (Country.UNITED_KINGDOM.value, 99.99, 4.99),
        (Country.UNITED_KINGDOM.value, 100.0, 0.0),
        (Country.FRANCE.value, 99.99, 8.99),
        (Country.FRANCE.value, 100.0, 4.99),
        (Country.ALBANIA.value, 99.99, 9.99),
        (Country.ALBANIA.value, 100.0, 9.99),
    ],
)
def test_shipping_calculates_correct_shipping_cost_for_uk(
    country: Country, order_total: float, shipping_cost: float
) -> None:
    result = calculate_shipping(country, order_total)

    assert result == shipping_cost
