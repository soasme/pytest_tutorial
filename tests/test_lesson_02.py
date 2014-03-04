# -*- coding: utf-8 -*-
"""
Fixture: addfinalizer
"""
import pytest

from model.user import User
import config

@pytest.fixture(scope="module")
def drop_db_file(request):
    def drop_file():
        import os
        os.remove(config.DBFILE)
    drop_file()
    request.addfinalizer(drop_file)

@pytest.fixture
def jack(request):
    # TODO: we should create user table at first and clean all data in user table at last
    # hint: request.addfinalizer
    # hint: call `User.create_table()` to create table `user`
    # hint: call `User.drop_table()` to drop table `user`
    return User.create(name='jack')

def test_user_created_success(jack):
    assert jack
    assert jack.id
    assert jack.name == 'jack'
