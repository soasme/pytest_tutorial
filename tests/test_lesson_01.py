# -*- coding: utf-8 -*-
"""
Fixture.
"""

import pytest
import datetime

from lib.time import mtimeformat, yesterdaytime

delta = datetime.timedelta
now = datetime.datetime.now


@pytest.fixture
def just_now():
    # TODO Please return a valid time (< 60 seconds)
    pass

def test_mtime_format_just_now(just_now):
    assert mtimeformat(just_now) == '刚刚'

def test_yesterdaytime_format_just_now(just_now):
    assert yesterdaytime(just_now) == '今天'
