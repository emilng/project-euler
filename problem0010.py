# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def sum_primes(num):
  values = range(3,num,2)
  prime_sum = 2
  while len(values) > 0:
    prime_sum = prime_sum + values[0]
    values = filter(lambda x: x % values[0] != 0, values)
  return prime_sum

print sum_primes(2000000)