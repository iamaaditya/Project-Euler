# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 21:43:35 2014

@author: aaditya prakash
"""

import utilities
import math
import time
import datetime
from dateutil.relativedelta import relativedelta

problem_number = '019'
problem_statement = """
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
1 Jan 1900 was Monday
"""

def Number_xdays_period(number, start, end):
    """ Returns the number of 'number' days (Monday = 0) since start date to
    end date (date in python datetime format) """
    totalDays = 0
    
    while start < end :
        #print start
        start += relativedelta(months=1)
        if start.weekday() == number: totalDays += 1        

    return totalDays
timeStart = time.clock()
print(Number_xdays_period(6, datetime.date(1901,1,1), datetime.date(2000, 12, 31)))
print('Time (sec):' + str(time.clock() - timeStart))
answer = '171'



