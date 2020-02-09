# -*- coding: utf-8 -*-
from django.db import transaction
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status
import ast
import json


def bytesToObjects(bytes):
    return ast.literal_eval(bytes.decode("utf-8"))

class TestModels(TestCase):

    def setUp(self):
        # 이곳에서 기본 셋팅
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def tearDown(self):
        # 이곳에서 종료 셋팅
        pass

    def test_model_order(self):
        url = '/blog/post/'
        response = self.client.get(url, {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(bytesToObjects(response.content), [])

        response = self.client.post(url, {"message": "message"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_dict = bytesToObjects(response.content)
        self.assertEqual(response_dict['message'], "message")

