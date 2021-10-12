# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# -*- coding: utf-8 -*-
import mock
import order.utils # <- 이렇게 지정해야 아래의 patch 에서 작동함
from django.test import TestCase
from mock import patch


class TestBlog(TestCase):
    def test(self):
        assert 1 == 2
