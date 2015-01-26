# Sum square difference

# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares(a, v):
  return a + v**2

def square_sum(nums):
  return sum(nums)**2

def sum_square_difference():
  nums = range(1,101)
  return square_sum(nums) - reduce(sum_squares, nums)

print sum_square_difference()