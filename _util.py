from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import gettz
import pytz


def time_to_seconds(t):
    if not t or not is_time_string(t):
        return 0
    convert = [3600, 60, 1]
    split = t.split(":")
    return sum(c * t for c, t in zip(convert[-1 * len(split):], map(int, split)))


epoch = pytz.utc.localize(datetime.utcfromtimestamp(0))
def unix_time(dt):
    return int((dt - epoch).total_seconds())


tzinfos = {"CST": gettz("America/Chicago")}
def parse_to_unix_time(s):
    dt = parse(s, tzinfos=tzinfos)
    if (dt.tzname() is None):
        dt = parse('{} CST'.format(s), tzinfos=tzinfos)
    return unix_time(dt)

def is_time_string(maybe_time):
    try:
        parse(maybe_time)
        return True
    except ValueError:
        return False
