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
def mock_address() -> Address:
    return Address(
        house="666",
        street="Street Name",
        city="City",
        postcode="postcode",
        country=Country.UNITED_KINGDOM,
    )


def test_order_add_item_successful(mock_item: Item, mock_address: Address) -> None:
    order = Order(shipping_address=mock_address, items=[])
    order.add_item(mock_item)

    assert len(order.items) == 1
    assert mock_item in order.items


def test_order_calculates_total_price(mock_item: Item, mock_address: Address) -> None:
    order = Order(shipping_address=mock_address, items=[mock_item])

    result = order.total_price

    assert result == 50



# def test_order_calculates_shipping_cost(
#     mock_item: Item, mock_address: Address
# ) -> None:
#     order = Order(shipping_address=mock_address, items=[mock_item])
#     order_total = 0
#     for item in order.items:
#         order_total += item.product.price * item.quantity
#
#     shipping_cost = 4.99
#
#     result = order.get_total_with_shipping_cost()
#
#     assert result == order_total + shipping_cost
