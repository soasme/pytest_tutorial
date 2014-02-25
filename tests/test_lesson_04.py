# -*- coding: utf-8 -*-
from lib.time import mtimeformat
import datetime

# Currently, It output like this:
#
#>       assert mtimeformat(datetime.datetime.now() == '1分钟前'
#        E       assert '\xe5\x88\x9a\xe5\x88\x9a' == '1\xe5\x88\x86\x...x9f\xe5\x89\x8d'
#        E         - \xe5\x88\x9a\xe5\x88\x9a
#        E         + 1\xe5\x88\x86\xe9\x92\x9f\xe5\x89\x8d)
#
# Please fill up tests/conftest.py `pytest_assertrepr_compare` for a better message:
#
#>       assert mtimeformat(datetime.datetime.now() == '1分钟前')
#E       assert String comparation
#E         刚刚 != 1分钟前
#
#
# Hint: an condition with returning ['String comparation', string.decode('utf8')]

def test_one_minutes_ago_with_better_assert_message():
    assert mtimeformat(datetime.datetime.now()) == '1分钟前'
