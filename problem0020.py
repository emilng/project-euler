# -*- coding: utf-8 -*-

# Factorial digit sum

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial(n):
  return reduce(lambda a, v: a * v ,range(1,n+1), 1)

digit_list = list(str(factorial(100)))
print reduce(lambda a, v: a + int(v), digit_list, 0)

