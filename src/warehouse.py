from dataclasses import dataclass
from typing import Self

from src.product import Product


@dataclass
class Entry:
    product: Product
    stock: int


@dataclass
class Warehouse:
    catalogue: list[Entry]

    def check_stock_level(self, product: Product) -> int:
        for entry in self.catalogue:
            if entry.product.id == product.id:
                return entry.stock

    def adjust_stock_level(self, product: Product, quantity: int) -> Self:
        for entry in self.catalogue:
            if self.check_stock_level(product) - quantity >= 0:
                entry.stock -= quantity

            else:
                print(f"Not enough stock to adjust product {product}")
