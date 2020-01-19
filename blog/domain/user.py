# -*- coding: utf-8 -*-
class User:
    def __init__(self, email, username):
        self.email = email
        self.username = username

    def __repr__(self):
        return "{}, {}".format(self.email, self.username)
