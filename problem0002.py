# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

p1 = 0
p2 = 1
n = 0
s = 0

while n < 4000000:
  n = p1 + p2
  if (n % 2 == 0):
    s = s + n
  p1 = p2
  p2 = n

print s