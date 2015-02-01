# -*- coding: utf-8 -*-

# Maximum path sum II

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt
# (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18.
# It is not possible to try every route to solve this problem,
# as there are 299 altogether! If you could check one trillion (1012) routes
# every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

def text_to_lines(text):
  return text.strip().split('\n')

def line_to_ints(line):
  return map(lambda item: int(item), line.strip().split(' '))

def text_to_ints(text):
  lines = text_to_lines(text)
  return map(line_to_ints, lines)

f = open('p067_triangle.txt')
text = f.read()
f.close()

triangle = text_to_ints(text)

def max_pairs(nums):
  i = 0
  last = len(nums) - 1
  pairs = []
  while i < last:
    pairs.append(max(nums[i], nums[i+1]))
    i = i + 1
  return pairs

def add_lines(top_line, bottom_line):
  i = 0
  length = len(top_line)
  added_lines = []
  while i < length:
    added_lines.append(top_line[i] + bottom_line[i])
    i = i + 1
  return added_lines

def max_totals(triangle):
  i = len(triangle) - 1
  added_lines = []
  max_line = []
  while i >= 0:
    line = triangle[i]
    if len(added_lines) > 0:
      max_line = max_pairs(added_lines)
      added_lines = add_lines(line, max_line)
    else:
      added_lines = line
    i = i - 1
  return added_lines[0]

print max_totals(triangle)