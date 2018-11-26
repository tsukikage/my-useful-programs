"""
removeCitations.py
Takes a copy-pasted text file 'file.txt' from Wikipedia, removes all bracketed
citations, and outputs it as a new 'file CR.txt' (CR = citations removed).
Written by Ellie Wix (elliewix) for, and with modifications by,
Nastassja Riemermann (tsukikage)
18-11-25
"""

IFILE = 'AI history.txt'

import re

ofile = IFILE[:-4]+' CR.txt'

with open(IFILE, 'r', encoding='utf-8') as fin:
    text = fin.read()

citation = re.compile('['+r'[0-9]+'+']')
text = re.sub(citation, '', text)

import io
with io.open(ofile, "w", encoding="utf-8") as f:
    f.write(text)