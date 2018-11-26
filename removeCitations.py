"""
removeCitations.py
Takes a copy-pasted text file 'file.txt' from Wikipedia, removes all bracketed
citations, and outputs it as a new 'file CR.txt' (CR = citations removed).
Written by Ellie Wix (elliewix) for, and with modifications by,
Nastassja Riemermann (tsukikage)
18-11-25
"""

# input file (to be edited by user as needed)
IFILE = 'AI history.txt'

# import statements
import re
import io

# generate output filename with " CR" appended to the end
ofile = IFILE[:-4]+' CR.txt'

# read input file
with open(IFILE, 'r', encoding='utf-8') as fin:
    text = fin.read()

# remove all citations
citation = re.compile('['+r'[0-9]+'+']')
text = re.sub(citation, '', text)

# crete output file (if needed) and write new version without citations
with io.open(ofile, "w", encoding="utf-8") as f:
    f.write(text)