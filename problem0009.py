# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def product_pythagorean_triplet(num):
  a = 1
  b = 2
  c = 3
  while a < num:
    while b < num:
      while c < num:
        if ((a + b + c == 1000) and (a**2 + b**2 == c**2)):
          return a * b * c
        c = c + 1
      b = b + 1
      c = b + 1
    a = a + 1
    b = a + 1
    c = b + 1

print product_pythagorean_triplet(1000)