# -*- coding: utf-8 -*-
"""
Fixture params
"""
import pytest
import datetime

from lib.time import mtimeformat

delta = datetime.timedelta
now = datetime.datetime.now


@pytest.fixture(
    # TODO return 60s ago & 61s ago & 119s ago
    # hint: use `params`
    # hint: http://pytest.org/latest/fixture.html#parametrizing-a-fixture
)
def one_minutes_ago(request):
    return mtimeformat(request.param)

def test_one_minutes_ago(one_minutes_ago):
    assert one_minutes_ago == '1分钟前'

@pytest.mark.parametrize(
    "time, expected", [
        # time, expected
        # 61s ago, 1分钟前

        # 121s ago, 2分钟前

        # 10001 ago, 2小时前

    ]
)
def test_minutes_ago(time, expected):
    assert mtimeformat(time) == expected
