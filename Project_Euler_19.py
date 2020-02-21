#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Project 19
# Credit to : http://radiusofcircle.blogspot.com

import time,calendar
calendar.setfirstweekday(6)

def sundays(year):
    """This function returns 
    The number of sundays in a year
    on the first of the month"""
    counter = 0
    for month in range(1,13):
        cal = calendar.monthcalendar(year,month)
        if cal[0][0]:
            counter += 1
        return counter

total = 0
for i in range(1901,2001):
    total += sundays(i)

print("Total Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000) is : "
+ str(total))

