from dataclasses import dataclass
from src.order import Order


@dataclass
class SalesHistory:
    orders: list[Order]

    def update(self, order: Order) -> None:
        self.orders.append(order)
