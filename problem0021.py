# -*- coding: utf-8 -*-

# Amicable numbers

# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an
# amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


def d(n):
  end = n
  i = 2
  divisors = [1]
  while i < end:
    if n % i == 0:
      end = n/i
      divisors.append(i)
      divisors.append(end)
    i = i + 1
  return sum(divisors)

sums = []
amicable = []

for i in range(0, 10001):
  sums.append(d(i))

for i in range(1, 10000):
  first_sum = sums[i]
  if (first_sum < len(sums)):
    second_sum = sums[first_sum]
    if (i == second_sum and i != first_sum):
      amicable.append(i)

print amicable
print sum(amicable)


