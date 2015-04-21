# -*- coding: utf-8 -*-

# Names scores

# Using names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import string

f = open('p022_names.txt')
text = f.read()
f.close()

text = text.replace('"','')
name_list = text.split(',')

uppercase_letters = string.ascii_uppercase

sorted_names = sorted(name_list)
name_count = len(sorted_names)
name_scores = []

for i in range(0, name_count):
  name = sorted_names[i]
  name_score = sum(map(lambda char: uppercase_letters.index(char) + 1, name)) * (i+1)
  name_scores.append(name_score)

print(sum(name_scores))


