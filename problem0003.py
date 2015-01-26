# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

factors = set([600851475143])

iterations = 0

# find largest factor and try to factor that
# repeat until largest factor can't be factored
# start at 3 and add 2 to each number because primes are always odd

def largest_prime_factor(factors):
  start = 3
  end = num = max(factors)
  while start < end:
    if (num % start == 0):
      factors.remove(num)
      factors.add(start)
      factors.add(num/start)
      return largest_prime_factor(factors)
    end = num/start
    start = start + 2
  return max(factors)

print largest_prime_factor(factors)

