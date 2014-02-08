# -*- coding: utf-8 -*-
"""
This is definition of ORM.

Model: All model base class.
database: a sqlite driver.
"""

__all__ = [
        'Model',
        'database',
        ]

from peewee import Model as PeeweeModel, SqliteDatabase
from config import DBFILE

database = SqliteDatabase(DBFILE)

class Model(PeeweeModel):
    class Meta:
        database = database
