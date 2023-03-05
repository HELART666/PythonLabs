# Get the current timestamp
import time
timestamp = time.time()

seconds = timestamp % 60
minutes = timestamp // 60 % 60
hours = timestamp // 3600 % 24
days = timestamp // 86400
months = timestamp // 2592000 % 12
years = timestamp // 31536000

year = 1970
month = 0
day = 0

hour = 0
minute = 0
second = 0

while days >= 365:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days -= 366
    else:
        days -= 365
    year += 1
    if day >= 0:
        month += 1


seconds_str = str(int(second))
minutes_str = str(int(minute))
hours_str = str(int(hour))
days_str = str(int(day))
months_str = str(int(month))
years_str = str(int(year))


if len(seconds_str) == 1:
    seconds_str = '0' + seconds_str
if len(minutes_str) == 1:
    minutes_str = '0' + minutes_str
if len(hours_str) == 1:
    hours_str = '0' + hours_str
if len(days_str) == 1:
    days_str = '0' + days_str
if len(months_str) == 1:
    months_str = '0' + months_str


date_str = years_str + '-' + months_str + '-' + days_str + ' ' + hours_str + ':' + minutes_str + ':' + seconds_str


print(date_str)
