from dataclasses import dataclass

from src.address import Address
from src.product import Product


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Order:
    shipping_address: Address
    items: list[Item]

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    @property
    def total_price(self) -> float:
        order_total = 0
        for item in self.items:
            order_total += item.product.price * item.quantity

        return order_total
