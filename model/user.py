# -*- coding: utf-8 -*-

from lib.orm import Model
from peewee import CharField

class User(Model):

    name = CharField()
