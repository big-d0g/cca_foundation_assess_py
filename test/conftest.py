import pytest

from src.countries import Country
from src.address import Address
from src.product import Product
from src.order import Item
from src.warehouse import Warehouse, Entry


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


@pytest.fixture
def mock_warehouse() -> Warehouse:
    entry_1 = Entry(
        product=Product(id=1, description="test product", price=10.00), stock=100
    )
    entry_2 = Entry(
        product=Product(id=2, description="another test product", price=50.00), stock=2
    )

    return Warehouse(catalogue=[entry_1, entry_2])
