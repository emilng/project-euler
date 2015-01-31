# -*- coding: utf-8 -*-

# Power digit sum

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def power_digit_sum(n):
  digit_list = list(str(2**n))
  return reduce(lambda a, v: a + int(v), digit_list, 0)

print power_digit_sum(1000)