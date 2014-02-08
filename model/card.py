# -*- coding: utf-8 -*-

import datetime
from lib.orm import Model
from peewee import CharField, TextField, IntegerField, DateTimeField

class Card(Model):

    user_id = IntegerField()
    title = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
