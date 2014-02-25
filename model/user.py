# -*- coding: utf-8 -*-

from lib.orm import Model
from peewee import CharField

class User(Model):

    name = CharField()

    def __repr__(self):
        return '<User id={0.id} name={0.name}>'.format(self)
