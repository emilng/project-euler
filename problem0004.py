# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def find_palindrome():
  palindromes = []
  first = 999
  while first > 0:
    second = 999
    while second > 0:
      num = first * second
      if (str(num) == str(num)[::-1]):
        palindromes.append(num)
      second = second - 1
    first = first - 1
  return max(palindromes)

print find_palindrome()