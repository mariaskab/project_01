 #!/usr/bin/env python
 # coding=utf-8
import datetime
number = int(input('Enter the month number:'))
month = int(number)

if int(month) < 1 or int(month) > 12:
 print('There is no such month')
pass
month = datetime.date(2023,month,1).strftime('%B')
if int(month) == 2:
    days_in_month = 28
    print("Вы ввели:", month_name, ",", days_in_month, "days")
