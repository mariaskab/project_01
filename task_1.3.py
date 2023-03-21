#!/usr/bin/env python
 # coding=utf-8
import datetime
number = int(input('Enter the month number:'))
if number < 1 or number > 12:
 print('There is no such month')
else:
    month = datetime.date(2023,number,1).strftime('%B')
print(month)