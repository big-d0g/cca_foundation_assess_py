import pytest

from src.address import Address
from src.countries import Country
from src.order import Order, Item
from src.product import Product


@pytest.fixture
def mock_item() -> Item:
    product = Product(id=1, description="test product", price=10.00)

    return Item(product=product, quantity=5)


@pytest.fixture
def mock_order(mock_item: Item) -> Order:
    address = Address(
        house="666",
        street="Street Name",
        city="City",
        postcode="postcode",
        country=Country.UNITED_KINGDOM,
    )
    return Order(shipping_address=address, items=[])


def test_order_add_item_successful(mock_item: Item, mock_order: Order) -> None:
    mock_order.add_item(mock_item)

    assert len(mock_order.items) == 1
    assert mock_item in mock_order.items
