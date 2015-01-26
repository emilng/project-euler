# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def divisible_by_nums(num, nums):
  for i in nums:
    if (num % i != 0):
      return False
  return True

def smallest_multiple():
  num = 20
  twenty_to_one = range(1,21)[::-1]
  while (divisible_by_nums(num, twenty_to_one) == False):
    num = num + 20
  return num

print smallest_multiple()