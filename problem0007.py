# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def is_prime(num, primes):
  for i in primes:
    if (num % i == 0):
      return False
  return True

def nth_prime(nth):
  primes = [3]
  count = 2
  i = 3
  while count < nth:
    if (is_prime(i, primes)):
      primes.append(i)
      count = count + 1
    i = i + 2
  return primes[-1]

print nth_prime(10001)