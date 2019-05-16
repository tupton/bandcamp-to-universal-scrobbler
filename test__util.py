from _util import time_to_seconds, is_time_string

import nose.tools as tools

def test_empty_time_to_seconds():
    tools.eq_(0, time_to_seconds(''))
    tools.eq_(0, time_to_seconds(None))

def test_time_to_seconds():
    tools.eq_(264, time_to_seconds("04:24"))

    tools.eq_(3600, time_to_seconds("1:00:00"))

def test_is_time_string():
    tools.eq_(False, is_time_string("Stare"))
    tools.eq_(True, is_time_string("04:24"))
    tools.eq_(True, is_time_string("1:00:00"))
