# -*- coding: utf-8 -*-
import re


def valid_str(str):
    p = re.compile('[A-Za-z]+')
    match_reg = p.match(str)
    if match_reg and match_reg.group() == str:
        return True
    else:
        return False


def a(temp_dict):
    temp_dict['test'] = "test"
    return temp_dict


def b():
    return a({})
