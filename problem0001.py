# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multiples(accumulator, value):
  if (value % 3 == 0 or value % 5 == 0):
    return accumulator + value
  else:
    return accumulator

# print sum_multiples(9, 10)
print reduce(sum_multiples, range(1000), 0)