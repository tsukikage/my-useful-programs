"""
textEnum.py
Takes a list of tuples of textbook chapters and the number of total examples,
definitions, theorems, corrolaries, etc., and outputs a text file that
enumerates each of these in the format chapter.number, separated by a space,
with a blank line between each chapter.
Written by Nastassja Riemermann (tsukikage)
18-11-24
"""

ch_ls = [(1,68),(2,45), (3,49), (4,36), (5,87), (6,45), (7,63), (8,55), (9,46)]
print_ls = []

for ch_tup in ch_ls:
    new_str = ""
    for idx in range(ch_tup[1]):
        new_str += "{}.{} ".format(ch_tup[0],idx+1)
    print_ls.append(new_str)

with open('text enum.txt', 'w') as f:
    for item in print_ls:
        f.write("%s\n\n" % item)