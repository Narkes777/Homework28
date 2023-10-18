# # Task 1
# import datetime

# # Текущая дата и время
# current_datetime = datetime.datetime.now()
# print("Текущая дата и время:", current_datetime)

# # Текущий год
# current_year = current_datetime.year
# print("Текущий год:", current_year)

# # Месяц года
# current_month = current_datetime.strftime("%B")
# print("Месяц года:", current_month)

# # Номер недели в году
# week_number = current_datetime.strftime("%U")
# print("Номер недели в году:", week_number)

# # Будний день недели
# weekday = current_datetime.strftime("%A")
# print("Будний день недели:", weekday)

# # День года
# day_of_year = current_datetime.timetuple().tm_yday
# print("День года:", day_of_year)

# # День месяца
# day_of_month = current_datetime.day
# print("День месяца:", day_of_month)

# # День недели
# day_of_week = current_datetime.weekday()
# print("День недели (0 - понедельник, 6 - воскресенье):", day_of_week)

# # Task 2
# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# year = int(input("Введите год: "))

# if leap_year(year):
#     print(f"{year} - високосный год")
# else:
#     print(f"{year} - невисокосный год")

# # Task 3
# from datetime import datetime

# input_str = "1 января 2014 14:43"

# months = {
#     'января': 1,
#     'февраля': 2,
#     'марта': 3,
#     'апреля': 4,
#     'мая': 5,
#     'июня': 6,
#     'июля': 7,
#     'августа': 8,
#     'сентября': 9,
#     'октября': 10,
#     'ноября': 11,
#     'декабря': 12
# }

# parts = input_str.split()
# day = int(parts[0])
# month = months[parts[1]]
# year = int(parts[2])
# time = parts[3]

# parsed_time = datetime.strptime(time, "%H:%M")

# result = datetime(year, month, day, parsed_time.hour, parsed_time.minute)

# formatted_result = result.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_result)

# # Task 4
# from datetime import datetime

# current_time = datetime.now()
# formatted_time = current_time.strftime("%H:%M:%S.%f")

# print(formatted_time)
