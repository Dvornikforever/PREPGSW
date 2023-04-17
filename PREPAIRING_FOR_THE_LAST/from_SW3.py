import datetime
import calendar

MONTHS = {'01': 'January',
          '02': 'February',
          '03': 'March',
          '04': 'April',
          '05': 'May',
          '06': 'June',
          '07': 'July',
          '08': 'August',
          '09': 'September',
          '10': 'October',
          '11': 'November',
          '12': 'December'}

periods = list(map(int, input().split()))
day, month, year = list(map(int, input().split('/')))
recent_date = datetime.date(year, month, day)
amount_of_dates_to_find = int(input())


def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
        while True:
            if (greater % x == 0) and (greater % y == 0):
                lcm = greater
                break
            greater += 1
        return lcm


LCM = calculate_lcm(*periods)

while amount_of_dates_to_find:
    recent_date += datetime.timedelta(days=LCM)
    if calendar.day_name[recent_date.weekday()] == 'Tuesday':
        continue
    else:
        print(
            f'{"0" + str(recent_date.day) if recent_date.day < 10 else recent_date.day}'
            f' {MONTHS["0" + str(recent_date.month) if recent_date.month < 10 else recent_date.year]}'
            f' {recent_date.year % 100}')
        amount_of_dates_to_find -= 1
