# -*- coding: utf-8 -*-
import mock
import order.utils # <- 이렇게 지정해야 아래의 patch 에서 작동함
from django.test import TestCase
from mock import patch


class TestMock(TestCase):

    # 함수의 리턴값을 강제로 패치
    @patch("order.utils.valid_str")
    def test_monkey_patch1(self, test_patch):
        test_patch.return_value = 'kihong'
        ret = order.utils.valid_str("")
        assert ret == "kihong"

    def test_monkey_patch2(self):
        assert order.utils.b() == {'test': 'test'}

    @mock.patch.object(order.utils, "a")
    def test_monkey_patch2(self, a):
        a.return_value = 'kihong'
        ret = order.utils.b()
        assert ret == "kihong"


