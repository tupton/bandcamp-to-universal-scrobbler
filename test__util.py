from _util import time_to_seconds

import nose.tools as tools

def test_empty_time_to_seconds():
    tools.eq_(0, time_to_seconds(''))
    tools.eq_(0, time_to_seconds(None))

def test_time_to_seconds():
    tools.eq_(264, time_to_seconds("04:24"))

    tools.eq_(3600, time_to_seconds("1:00:00"))
