# -*- coding: utf-8 -*-
from ..utils import valid_str


def test_valid_str():
    assert valid_str("test") is True
    assert valid_str("test ") is False
    assert valid_str("test1234") is not True
