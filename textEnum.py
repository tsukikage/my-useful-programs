"""
textEnum.py
Takes a list of tuples of textbook chapters and the number of total examples,
definitions, theorems, corrolaries, etc., and outputs a text file that
enumerates each of these in the format chapter.number, separated by a space,
with a blank line between each chapter.
Written by Nastassja Riemermann (tsukikage)
18-11-24
"""

# list of chapters and no. of examples, etc. (to be edited by user as needed)
CH_LS = [(1,68),(2,45), (3,49), (4,36), (5,87), (6,45), (7,63), (8,55), (9,46)]

# Generate enumeration of examples, etc., for each chapter which will be output.
# Each chapter is its own string, which is its own item in a list.
output_ls = []
for ch_tup in CH_LS:
    new_str = ""
    for idx in range(ch_tup[1]):
        new_str += "{}.{} ".format(ch_tup[0],idx+1)
    output_ls.append(new_str)

# Write the output list to "text enum.txt", with a blank line between each
# list element (chapter).
with open('text enum.txt', 'w') as f:
    for item in output_ls:
        f.write("%s\n\n" % item)