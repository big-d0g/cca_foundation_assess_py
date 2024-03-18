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


def test_warehouse_adjust_stock_level_updates_entry_of_requested_product() -> None:
    product = Product(id=1, description="test product", price=10.00)
    item = Item(product=product, quantity=50)
    entry = Entry(product=product, stock=100)
    warehouse = Warehouse(catalogue=[entry])

    expected_result = entry.stock - item.quantity

    warehouse.adjust_stock_level(item.product, item.quantity)

    assert entry.stock == expected_result
