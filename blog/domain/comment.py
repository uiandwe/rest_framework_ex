# -*- coding: utf-8 -*-
from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

    def __repr__(self):
        return "{}, {}, {}".format(self.email, self.content, self.created)
