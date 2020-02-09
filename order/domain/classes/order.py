# -*- coding: utf-8 -*-

from dataclasses import dataclass, field, asdict, astuple, make_dataclass
import enum
import typing
from .product import Product
from ..decorater.valid import Valid


class OrderState(enum.Enum):
    cancel : 0
    ready : 1
    completed_order : 2
    shipping : 3
    completed_shipping : 4

@dataclass
class Order(Valid):
    order_number: str
    total_amounts: int
    state: OrderState
    products: typing.List

    def __repr__(self):
        return self.__dict__

    def cancel(self):
        self.state = OrderState.cancel

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError

        self.products.append(product)

    def sum_products_price(self):
        self.total_amounts = sum(int(product.price) for product in self.products)
