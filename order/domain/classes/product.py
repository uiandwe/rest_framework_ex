# -*- coding: utf-8 -*-
from dataclasses import dataclass
from ..decorater.valid import Valid


@dataclass
class Product(Valid):
    name: str
    price: int

    def __repr__(self):
        return self.__dict__
