# -*- coding: utf-8 -*-

# Lattice paths

# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

#   __    _      _
#     |    |_     |
#     |      |    |_
#
#
#  |__    |_     |
#     |     |_   |__

# How many such routes are there through a 20×20 grid?

# a route can be represented with an
# x for each movement along x
# and a y for each movement along y
# so the 6 routes above can be represented
# with the following letter combinations
# xxyy xyxy xyyx yxxy yxyx yyxx

# the number of routes can be figured out using
# the formula for multiset permutations
# n!/(m1)! * (m2)! ... * (mn)!
# where n is the total number of elements
# and each m is a unique element multiplied
# by the number of times it appears
# which in this case would be (grid_size*2)!/(grid_size!)*(grid_size!)

def factorial(n):
  return reduce(lambda a, v: a * v ,range(1,n+1), 1)

def routes(grid_size):
  size_factorial = factorial(grid_size)
  double_size_factorial = factorial(grid_size * 2)
  return double_size_factorial/(size_factorial**2)

print routes(20)
