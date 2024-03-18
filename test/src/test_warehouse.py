import pytest

from src.product import Product
from src.warehouse import Warehouse, Entry
from src.order import Item


def test_warehouse_returns_correct_stock_level() -> None:
    entry = Entry(
        product=Product(id=1, description="test product", price=10.00), stock=100
    )

    warehouse = Warehouse(catalogue=[entry])

    result = warehouse.check_stock_level(entry.product)

    assert result == entry.stock


def test_warehouse_adjust_stock_level_updates_stock_when_valid_quantity_given() -> None:
    product = Product(id=1, description="test product", price=10.00)
    item = Item(product=product, quantity=50)
    entry = Entry(product=product, stock=100)
    warehouse = Warehouse(catalogue=[entry])

    expected_result = entry.stock - item.quantity

    warehouse.adjust_stock_level(item.product, item.quantity)

    assert entry.stock == expected_result


def test_warehouse_adjust_stock_raises_error_when_not_enough_products() -> None:
    product = Product(id=1, description="test product", price=10.00)
    item = Item(product=product, quantity=100)
    entry = Entry(product=product, stock=50)
    warehouse = Warehouse(catalogue=[entry])

    with pytest.raises(ValueError):
        warehouse.adjust_stock_level(item.product, item.quantity)


def test_warehouse_updates_catalogue_when_receives_new_stock_for_existing_product() -> (
    None
):
    product = Product(id=1, description="test product", price=10.00)
    item = Item(product=product, quantity=100)
    entry = Entry(product=product, stock=50)
    warehouse = Warehouse(catalogue=[entry])

    expected_result = entry.stock + item.quantity

    warehouse.receive_stock(item.product, item.quantity)

    assert len(warehouse.catalogue) == 1
    assert warehouse.catalogue[0].stock == expected_result
