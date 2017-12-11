#!/usr/bin/env python

"""
Convert an iTunes copied playlist to a CSV that can be used with Universal Scrobbler's bulk import.

Usage:
    itunes-to-universal-scrobbler.py <playlist>

    playlist The copied playlist entries from iTunes
"""

from __future__ import print_function

from docopt import docopt
import re
from _util import time_to_seconds

__version__ = "0.1.0"

def parse(args):
    for line in args.get("<playlist>").strip().split('\n'):
        parts = re.split(r'\t+', line.strip())
        yield '"{artist}", "{track}", "{album}", "", "", "{duration}"'.format(artist=parts[2], track=parts[0], album=parts[3], duration=time_to_seconds(parts[1]))


if __name__ == "__main__":
    arguments = docopt(__doc__, version="iTunes to Universal Scrobbler {}".format(__version__))
    for line in parse(arguments):
        print("{}".format(line))
