# Sum square difference

# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference():
  nums = range(1,101)
  square_sum = sum(nums)**2
  sum_squares = reduce(lambda a, v: a + v**2, nums)
  return square_sum - sum_squares

print sum_square_difference()