# -*- coding: utf-8 -*-

# Number letter counts

# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


def nums_to_words(num):
  ones_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  tens_words = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
  teens_words = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

  num_list = map(lambda x: int(x), list(str(num)))[::-1]
  # print num_list
  ones = tens = hundreds = thousands = ''
  if num_list[0] > 0:
    # print num_list[0]
    ones = ones_words[num_list[0]-1]
  if len(num_list) > 1 and num_list[1] == 1 and num_list[0] > 0:
    ones = ''
    tens = teens_words[num_list[0]-1]
  elif len(num_list) > 1 and num_list[1] > 0:
    tens = tens_words[num_list[1]-1]
  if len(num_list) > 2 and num_list[2] > 0:
    hundreds = ones_words[num_list[2]-1] + 'hundred'
    if tens != '' or ones != '':
      hundreds = hundreds + 'and'
  if len(num_list) > 3 and num_list[3] > 0:
    thousands = ones_words[num_list[3]-1] + 'thousand'
    if hundreds != '' or tens != '' or ones != '':
      thousands = thousands + 'and'
  # print thousands + hundreds + tens + ones
  return thousands + hundreds + tens + ones

def char_count(num):
  return reduce(lambda a, v: a + len(nums_to_words(v)), range(1, num + 1), 0)

map(nums_to_words, range(1, 1001))
# print len(nums_to_words(342))
# print len(nums_to_words(115))
print char_count(1000)
