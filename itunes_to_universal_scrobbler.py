#!/usr/bin/env python

"""
Convert an iTunes copied playlist to a CSV that can be used with Universal Scrobbler's bulk import.

Usage:
    itunes-to-universal-scrobbler.py [--start-time=<start-time>] <playlist>

    playlist                  The copied playlist entries from iTunes
    --start-time=<start-time> A time string to indicate the timestamp of the first track
"""

from __future__ import print_function

from docopt import docopt
import re
import sys
from datetime import datetime
from _util import time_to_seconds, parse_to_unix_time

__version__ = "0.1.0"

def parse(args):
    try:
        start_time = parse_to_unix_time(args.get("--start-time"))
        track_start = start_time
    except (ValueError, TypeError):
        start_time = None
        track_start = 0
    prev_duration = 0
    for line in args.get("<playlist>").strip().split('\n'):
        parts = re.split(r'\t+', line.strip())
        if start_time is None:
            ts = ""
        else:
            track_start = track_start + prev_duration
            ts = datetime.fromtimestamp(track_start)
        duration = time_to_seconds(parts[1])
        prev_duration = duration

        yield '"{artist}", "{track}", "{album}", "{ts}", "", "{duration}"'.format(artist=parts[2], track=parts[0], album=parts[3], ts=ts, duration=duration)


if __name__ == "__main__":
    arguments = docopt(__doc__, version="iTunes to Universal Scrobbler {}".format(__version__))
    for line in parse(arguments):
        print("{}".format(line))
