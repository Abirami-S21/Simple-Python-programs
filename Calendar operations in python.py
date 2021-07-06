#!/usr/bin/env python
# coding: utf-8

# In[3]:


#To find the day for the given date in python

#import the calendar module in python
import calendar

#Enter the date in month, date and year format as mm,dd,year as space separated integers
print("Enter the date in month, date and year format as mm,dd,year as space separated integers")
mm,dd,year=map(int,input().split())
day=calendar.weekday(year,mm,dd)


#to print the day in uppercase
print(calendar.day_name[day].upper()) 


# In[ ]:




