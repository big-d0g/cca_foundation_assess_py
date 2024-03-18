from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from src.warehouse import Warehouse
from src.address import Address
from src.product import Product
from src.shipping import calculate_shipping


class Status(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Order:
    shipping_address: Address
    items: list[Item]
    status: Status = Status.PENDING

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

    def confirm(self, warehouse: Warehouse, sales_history: "SalesHistory") -> None:
        for entry in warehouse.catalogue:
            for item in self.items:
                if (
                    item.product.id == entry.product.id
                    and entry.stock - item.quantity >= 0
                ):
                    entry.stock -= item.quantity

                    self.status = Status.CONFIRMED

                    if sales_history:
                        sales_history.update(self)
                else:
                    print(f"{item.product} is not available")
