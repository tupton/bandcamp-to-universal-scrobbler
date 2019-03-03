#!/usr/bin/env python

"""
Convert a Bandcamp track listing to a CSV that can be used with Universal Scrobbler's bulk import.

Usage:
    bandcamp-to-universal-scrobbler.py [--start-time=<start-time>] <artist> <album> <track-listing>

    artist                    The artist as a string
    album                     The album name as a string
    track-listing             The copied track listing from a Bandcamp page
    --start-time=<start-time> A time string to indicate the timestamp of the first track
"""

from __future__ import print_function
try:
    from future_builtins import filter
except ImportError:
    pass

from docopt import docopt
import re
import sys
from datetime import datetime
from _util import time_to_seconds, parse_to_unix_time

__version__ = "0.1.0"

def _filter_detritus(track_line):
    clean = track_line.strip().lower()
    disallowed = {'lyrics', 'buy track', 'info', 'video'}
    return clean not in disallowed;

def filter_track_lines(track_lines):
    track_number_re = re.compile(r"^\d+\.$")
    return filter(lambda line: line and line.strip() != "" and track_number_re.search(line) is None and _filter_detritus(line), track_lines)

def parse(args):
    artist = args.get("<artist>")
    album = args.get("<album>")
    tracks = args.get("<track-listing>").split("\n")

    try:
        start_time = parse_to_unix_time(args.get("--start-time"))
        track_start = start_time
    except (ValueError, TypeError):
        start_time = None
        track_start = 0
    prev_duration = 0

    for line in filter_track_lines(tracks):
        track, time = line.rsplit(" ", 1)

        # Sometimes the track line has cruft at the end, e.g. "video"
        if not _filter_detritus(time):
            track, time = track.rsplit(" ", 1)

        if start_time is None:
            ts = ""
        else:
            track_start = track_start + prev_duration
            ts = datetime.fromtimestamp(track_start)
        duration = time_to_seconds(time)
        prev_duration = duration

        yield '"{artist}", "{track}", "{album}", "{ts}", "", "{duration}"'.format(artist=artist, track=track, album=album, ts=ts, duration=duration)


if __name__ == "__main__":
    arguments = docopt(__doc__, version="Bandcamp to Universal Scrobbler {}".format(__version__))
    for line in parse(arguments):
        print("{}".format(line))
