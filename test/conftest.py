import pytest

from src.countries import Country
from src.address import Address
from src.product import Product
from src.order import Item


@pytest.fixture
def mock_item() -> Item:
    product = Product(id=1, description="test product", price=10.00)

    return Item(product=product, quantity=5)


@pytest.fixture
def mock_address() -> Address:
    return Address(
        house="666",
        street="Street Name",
        city="City",
        postcode="postcode",
        country=Country.UNITED_KINGDOM,
    )
