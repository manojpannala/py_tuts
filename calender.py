import calendar

print(calendar.calendar(2021))

# if it is a leap year

is_leap = calendar.isleap(2021)
print("Is it a leap year:", is_leap)

# No. of leap days since 2000 - 2021

no_leap_days = calendar.leapdays(2000, 2021)
print ('No. of Leap days from 2000 to 2021:', no_leap_days)