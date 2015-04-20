# -*- coding: utf-8 -*-

# Counting Sundays

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# loop through years
# loop through months
# loop through days in months
# count through days of the week in each month

# 30 day months = 4, 6, 9, 11


year = 1900
# monday is the second day of the week
day_of_the_week = 2
first_sundays = 0

for year in range(1900,2001):
  print year
  for month in range(1, 13):
    if month == 4 or month == 6 or month == 9 or month == 11:
      num_days = 30
    elif month == 2:
      num_days = 28
      if year % 100 == 0 and year % 400 == 0:
        num_days = 29
      elif year % 100 != 0 and year % 4 == 0:
        num_days = 29
    else:
      num_days = 31
    for day in range(1, num_days + 1):
      print year, month, day, day_of_the_week
      if year > 1900 and day == 1 and day_of_the_week == 1:
        first_sundays = first_sundays + 1
      if day_of_the_week < 7:
        day_of_the_week = day_of_the_week + 1
      else:
        day_of_the_week = 1

print 'first sundays', first_sundays

