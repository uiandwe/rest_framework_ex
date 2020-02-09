# -*- coding: utf-8 -*-
from django.db import transaction
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient

from ..models import Order, Product


class TestModels(TestCase):

    def setUp(self):
        # 이곳에서 기본 셋팅
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.obj = Order.objects.create(order_name='Creation of Adam')
        self.p1 = Product.objects.create(name="p1", price=1000)
        self.p2 = Product.objects.create(name="p2", price=2000)

    def tearDown(self):
        # 이곳에서 종료 셋팅
        Order.objects.all().delete()
        Product.objects.all().delete()

    def test_model_order(self):
        o1 = Order.objects.get(id=1)
        self.assertTrue(self.obj, o1)

        with transaction.atomic():
            #total_amount 는 int형
            try:
                order_obj = Order.objects.create(order_name="aasdf", total_amount="adf")
            except Exception as e:
                assert isinstance(e, ValueError)

    def test_model_product(self):
        assert self.p1.name == "p1"
        temp_p = Product.objects.get(id=1)
        assert self.p1 == temp_p

    def test_model_product2(self):
        temp_p = Product.objects.get(id=1)
        assert temp_p.name == "p1"
        return temp_p

