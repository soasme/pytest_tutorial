# -*- coding: utf-8 -*-
"""
Fixture.
"""

import pytest
import datetime

from lib.time import mtimeformat

delta = datetime.timedelta
now = datetime.datetime.now


@pytest.fixture
def just_now():
    # TODO Please return a valid time (< 60 seconds)
    pass

def test_just_now(just_now):
    assert mtimeformat(just_now) == '刚刚'
