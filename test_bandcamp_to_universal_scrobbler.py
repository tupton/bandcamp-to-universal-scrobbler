from bandcamp_to_universal_scrobbler import filter_track_lines, parse

import nose.tools as tools

def test_empty_filter_track_lines():
    tools.eq_(0, sum(1 for _ in filter_track_lines([])))
    tools.eq_(0, sum(1 for _ in filter_track_lines(['', None])))

def test_filter_track_lines():
    lines = """1.
Emotional Weightlessness 04:24
2.
Conversational Gravity 06:00
3.
That Which Will Be, And That Which Will Not 04:50
4.
End All, Be All 04:44
5.
Giant Arthropod Creature 07:55
6.
Hapless 02:26
7.
Weight Of The Word 06:29
"""
    filter_iter = filter_track_lines(lines.split("\n"))
    tools.eq_(7, sum(1 for _ in filter_iter))

    # filter empty line and no track number at start of input
    lines="""
Tribulation 01:35
2.
To Ruin A Fine Tenor Voice 03:27
lyrics
3.
Concrete Blocks of Empathy 05:08
4.
Careworn 06:01
5.
Entr'acte 04:23
6.
We Have Not Reached Conclusion 03:45
"""
    filter_iter = filter_track_lines(lines.split("\n"))
    tools.eq_(6, sum(1 for _ in filter_iter))

def test_parse():
    args = {
        "<artist>": "Frequency Eater",
        "<album>": "Finite States",
        "<track-listing>": """1.
Emotional Weightlessness 04:24
2.
Conversational Gravity 06:00
3.
That Which Will Be, And That Which Will Not 04:50
4.
End All, Be All 04:44
5.
Giant Arthropod Creature 07:55
6.
Hapless 02:26
7.
Weight Of The Word 06:29
"""
    }

    expected = """
"Frequency Eater", "Emotional Weightlessness", "Finite States", "", "", "264"
"Frequency Eater", "Conversational Gravity", "Finite States", "", "", "360"
"Frequency Eater", "That Which Will Be, And That Which Will Not", "Finite States", "", "", "290"
"Frequency Eater", "End All, Be All", "Finite States", "", "", "284"
"Frequency Eater", "Giant Arthropod Creature", "Finite States", "", "", "475"
"Frequency Eater", "Hapless", "Finite States", "", "", "146"
"Frequency Eater", "Weight Of The Word", "Finite States", "", "", "389"
""".strip()

    tools.eq_(expected, "\n".join(line for line in parse(args)))
