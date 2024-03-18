from src.product import Product
from src.warehouse import Warehouse, Entry


def test_warehouse_returns_correct_stock_level() -> None:
    product = Product(id=1, description="test product", price=10.00)
    entry = Entry(
        product=product, stock=100
    )

    warehouse = Warehouse(catalogue=[entry])

    result = warehouse.check_stock_level(product)

    assert result == entry.stock
