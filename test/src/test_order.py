from src.address import Address

from src.order import Order, Item, Status


def test_order_add_item_successful(mock_item: Item, mock_address: Address) -> None:
    order = Order(shipping_address=mock_address, items=[])
    order.add_item(mock_item)

    assert len(order.items) == 1
    assert mock_item in order.items


def test_order_calculates_total_price(mock_item: Item, mock_address: Address) -> None:
    order = Order(shipping_address=mock_address, items=[mock_item])

    result = order.total_price

    assert result == 50


def test_order_calculates_shipping_cost(mock_item: Item, mock_address: Address) -> None:
    order = Order(shipping_address=mock_address, items=[mock_item])

    result = order.shipping_cost

    assert result == 4.99


def test_order_get_total_including_shipping_successful(
    mock_item: Item, mock_address: Address
) -> None:
    order = Order(shipping_address=mock_address, items=[mock_item])

    result = order.get_total_price_including_shipping()

    assert result == 54.99


def test_order_status_updates_on_confirmation(
    mock_item: Item, mock_address: Address
) -> None:
    order = Order(shipping_address=mock_address, items=[mock_item])

    assert order.status == Status.PENDING

    order.confirm()

    assert order.status == Status.CONFIRMED
