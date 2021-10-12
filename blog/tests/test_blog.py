# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.test import TestCase


class TestBlog(TestCase):
    def test(self):
        assert 1 == 1


class MyTest(TestCase):
    fixtures = ["user.json"]  # fixtures폴더의 user.json으로 데이터 생성

    def test_should_create_group(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, "admin")
