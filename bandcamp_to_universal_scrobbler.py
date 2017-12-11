#!/usr/bin/env python

"""
Convert a Bandcamp track listing to a CSV that can be used with Universal Scrobbler's bulk import.

Usage:
    bandcamp-to-universal-scrobbler.py <artist> <album> <track-listing>

    artist        The artist as a string
    album         The album name as a string
    track-listing The copied track listing from a Bandcamp page
"""

from __future__ import print_function

from itertools import ifilter
from docopt import docopt
from _util import time_to_seconds
import re

__version__ = "0.1.0"

def filter_track_lines(track_lines):
    track_number_re = re.compile(r"^\d+\.$")
    return ifilter(lambda line: line and track_number_re.search(line) is None, track_lines)

def parse(args):
    artist = args.get("<artist>")
    album = args.get("<album>")
    tracks = args.get("<track-listing>").split("\n")

    for line in filter_track_lines(tracks):
        track, time = line.rsplit(" ", 1)
        duration = time_to_seconds(time)
        yield '"{artist}", "{track}", "{album}", "", "", "{duration}"'.format(artist=artist, track=track, album=album, duration=duration)


if __name__ == "__main__":
    arguments = docopt(__doc__, version="Bandcamp to Universal Scrobbler {}".format(__version__))
    for line in parse(arguments):
        print("{}".format(line))
