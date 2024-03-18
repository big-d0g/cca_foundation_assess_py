from src.address import Address

from src.order import Order, Item, Status
from src.warehouse import Warehouse


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
    mock_item: Item, mock_address: Address, mock_warehouse: Warehouse
) -> None:
    order = Order(shipping_address=mock_address, items=[mock_item])

    assert order.status == Status.PENDING

    order.confirm(mock_warehouse)

    assert order.status == Status.CONFIRMED


def test_order_updates_warehouse_stock_amount_if_success(
    mock_item: Item, mock_warehouse: Warehouse, mock_address: Address
) -> None:
    order = Order(shipping_address=mock_address, items=[mock_item])

    expected_result = mock_warehouse.catalogue[0].stock - mock_item.quantity

    order.confirm(mock_warehouse)

    assert mock_warehouse.catalogue[0].product.id == mock_item.product.id
    assert mock_warehouse.catalogue[0].stock == expected_result


def test_order_does_not_confirm_if_not_enough_stock(
    mock_item: Item, mock_warehouse: Warehouse, mock_address: Address
) -> None:
    mock_item.quantity = 1000
    order = Order(shipping_address=mock_address, items=[mock_item])

    stock_before_order = mock_warehouse.catalogue[0].stock

    order.confirm(mock_warehouse)

    assert order.status == Status.PENDING
    assert mock_warehouse.catalogue[0].product.id == mock_item.product.id
    assert mock_warehouse.catalogue[0].stock == stock_before_order
