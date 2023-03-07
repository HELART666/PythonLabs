import time

timestamp = time.time()


month_days = [31,28,31,30,31,30,31,31,30,31,30,31]


months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

year = 1970
day = 0
month = 0
while True:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_days[1] = 29
    else:
        month_days[1] = 28
    if day + month_days[month] > (timestamp / 86400):
        break
    else:
        day += month_days[month]
        month += 1
        if month == 12:
            month = 0
            year += 1

day_of_month = int((timestamp / 86400 - day) % month_days[month]) + 1
hours = int((timestamp % 86400) // 3600)
minutes = int((timestamp % 3600) // 60)
seconds = int(timestamp % 60)

date_str = f"{year:04d}-{month+1:02d}-{day_of_month:02d} {hours:02d}:{minutes:02d}:{seconds:02d}"
print(date_str)

