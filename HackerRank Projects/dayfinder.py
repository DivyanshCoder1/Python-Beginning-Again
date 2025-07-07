import calendar
from datetime import date

user_date_string = list(input("> ").split(" "))
user_date_int = [int(item) for item in user_date_string]

date_obj = date(user_date_int[2], user_date_int[0], user_date_int[1])

week_day_index = date.weekday(date_obj)

day_name = calendar.day_name[week_day_index]

print(day_name.upper())