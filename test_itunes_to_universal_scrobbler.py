from itunes_to_universal_scrobbler import parse

import nose.tools as tools

def test_parse():
    args = {
        "<playlist>": """Porcelain		3:13	Hundredth	RARE B-Sides - Single	Rock	0	
Bound		3:13	Hail the Sun	Secret Wars - EP	Rock	0	
Guillotinas		3:15	Viva Belgrado	Guillotinas - Single	Electronic	0	
(Telebrothy)		2:11	Demons	Embrace Wolf	Alternative	2	1
Hope Is Lost		4:34	Open Hand	Hope Is Lost - Single	Alternative	0	
Ghosts of Former Lives		3:54	Icarus The Owl	Rearm Circuits	Alternative	0	
Swans		3:12	Heal	No Love / No Light	Rock	2	
The Ponytail Parade (Reimagined)		3:54	Emery	Revival: Emery Classic Reimagined	Rock	0	
Doubt Mines		2:38	Terrible Love	Doubt Mines - Single	Alternative	0	
Deserted Dunes Welcome Weary Feet		3:34	King Gizzard & The Lizard Wizard	Polygondwanaland	Alternative	2	
Northern Skin		4:17	Actor Observer	One Another - Single	Heavy Metal	2	
To Venomous Depths / Where No Light Shines		7:53	Cloak	To Venomous Depths	Heavy Metal	2	
The Grave		3:27	Tracy Bryant	A Place for Nothing and Everything in Its Place	Indie Rock	0	
To Be Given a Body		8:04	TORRES	Three Futures	Alternative	0	
Asktell (Audiotree Live Version)		2:56	Lina Tullgren	Lina Tullgren on Audiotree Live - EP	Singer/Songwriter	0	
Whispers From the Surface of a Lake		2:43	Hior Chronik	Out of the Dust	Modern Era	0	
Old Anew		7:21	Ensemble, Et Al.	The Slow Reveal	Electronic	0	
Luxury		2:17	Martyn Heyne	Electric Intervals	Contemporary Era	0	
Secret Life of Waves		3:14	Robert Haigh	Creatures of the Deep	Ambient	0	
Blue Eyes Reflection		5:03	Vanity Productions	Only the Grains of Love Remain	Electronic	0	
One With You		2:29	Backtrack	Bad To My World	Punk	0	
Coming To		2:27	Hangman	A Vile Decree - EP	Rock	0	
Shattering		2:28	Sincere Engineer	Rhombithian	EMO	0	
Moon Curser		8:27	Dead Quiet	Grand Rites	Heavy Metal	0	
Freedom		3:01	Bib	Moshpit - EP	Alternative	0	
"""
    }

    expected = """
"Hundredth", "Porcelain", "RARE B-Sides - Single", "", "", "193"
"Hail the Sun", "Bound", "Secret Wars - EP", "", "", "193"
"Viva Belgrado", "Guillotinas", "Guillotinas - Single", "", "", "195"
"Demons", "(Telebrothy)", "Embrace Wolf", "", "", "131"
"Open Hand", "Hope Is Lost", "Hope Is Lost - Single", "", "", "274"
"Icarus The Owl", "Ghosts of Former Lives", "Rearm Circuits", "", "", "234"
"Heal", "Swans", "No Love / No Light", "", "", "192"
"Emery", "The Ponytail Parade (Reimagined)", "Revival: Emery Classic Reimagined", "", "", "234"
"Terrible Love", "Doubt Mines", "Doubt Mines - Single", "", "", "158"
"King Gizzard & The Lizard Wizard", "Deserted Dunes Welcome Weary Feet", "Polygondwanaland", "", "", "214"
"Actor Observer", "Northern Skin", "One Another - Single", "", "", "257"
"Cloak", "To Venomous Depths / Where No Light Shines", "To Venomous Depths", "", "", "473"
"Tracy Bryant", "The Grave", "A Place for Nothing and Everything in Its Place", "", "", "207"
"TORRES", "To Be Given a Body", "Three Futures", "", "", "484"
"Lina Tullgren", "Asktell (Audiotree Live Version)", "Lina Tullgren on Audiotree Live - EP", "", "", "176"
"Hior Chronik", "Whispers From the Surface of a Lake", "Out of the Dust", "", "", "163"
"Ensemble, Et Al.", "Old Anew", "The Slow Reveal", "", "", "441"
"Martyn Heyne", "Luxury", "Electric Intervals", "", "", "137"
"Robert Haigh", "Secret Life of Waves", "Creatures of the Deep", "", "", "194"
"Vanity Productions", "Blue Eyes Reflection", "Only the Grains of Love Remain", "", "", "303"
"Backtrack", "One With You", "Bad To My World", "", "", "149"
"Hangman", "Coming To", "A Vile Decree - EP", "", "", "147"
"Sincere Engineer", "Shattering", "Rhombithian", "", "", "148"
"Dead Quiet", "Moon Curser", "Grand Rites", "", "", "507"
"Bib", "Freedom", "Moshpit - EP", "", "", "181"
""".strip()

    tools.eq_(expected, "\n".join(line for line in parse(args)))
