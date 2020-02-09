# -*- coding: utf-8 -*-
from ..classes.product import Product
from ..classes.order import Order

class ProductOrder:
    def create_product(self, name, price):
        try:
            product = Product(name=name, price=price)
        except Exception as e:
            print(e)
            return None

        return product

    # def get_products(self):
    #
    #
    # def create_orders(self):

