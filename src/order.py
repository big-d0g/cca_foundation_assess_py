from dataclasses import dataclass

from src.address import Address
from src.product import Product
from src.shipping import calculate_shipping


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

    @property
    def shipping_cost(self) -> float:
        return calculate_shipping(self.shipping_address.country.value, self.total_price)

    def get_total_price_including_shipping(self) -> float:
        return self.total_price + self.shipping_cost
