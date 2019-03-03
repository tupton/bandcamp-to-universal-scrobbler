# Bandcamp to Universal Scrobbler

[![CircleCI Build Status](https://circleci.com/gh/tupton/bandcamp-to-universal-scrobbler/tree/master.svg?style=svg)](https://circleci.com/gh/tupton/bandcamp-to-universal-scrobbler/tree/master)

Convert a copied track listing from [a Bandcamp release page][bc] to a CSV that can be used in [Universal Scrobbler's bulk scrobbler][us].

  [bc]: https://aviatorma.bandcamp.com/album/loneliness-leaves-the-light-on-for-me
  [us]: http://universalscrobbler.com/bulk.php

E.g.

```bash
❯ python bandcamp_to_universal_scrobbler.py "Aviator" "Loneliness Leaves The Light On For Me" "1.
I Wanna Make Movies, Heather 02:36
2.
Nasonov Pheromone 03:06
3.
Ad Nauseam 04:19
4.
I Wouldn't Leave Here If You Paid Me 04:30
5.
Looks Deep Enough From Here 04:38
6.
End Scene 03:03
7.
One Year Warranty 02:09
8.
I Wouldn't Live There If You Paid Me 02:35
9.
Safety Coffin 04:03
10.
Does It Make A Sound? 03:40"
"Aviator", "I Wanna Make Movies, Heather", "Loneliness Leaves The Light On For Me", "", "", "156"
"Aviator", "Nasonov Pheromone", "Loneliness Leaves The Light On For Me", "", "", "186"
"Aviator", "Ad Nauseam", "Loneliness Leaves The Light On For Me", "", "", "259"
"Aviator", "I Wouldn't Leave Here If You Paid Me", "Loneliness Leaves The Light On For Me", "", "", "270"
"Aviator", "Looks Deep Enough From Here", "Loneliness Leaves The Light On For Me", "", "", "278"
"Aviator", "End Scene", "Loneliness Leaves The Light On For Me", "", "", "183"
"Aviator", "One Year Warranty", "Loneliness Leaves The Light On For Me", "", "", "129"
"Aviator", "I Wouldn't Live There If You Paid Me", "Loneliness Leaves The Light On For Me", "", "", "155"
"Aviator", "Safety Coffin", "Loneliness Leaves The Light On For Me", "", "", "243"
"Aviator", "Does It Make A Sound?", "Loneliness Leaves The Light On For Me", "", "", "220"
```
