from datetime import datetime

year = int(input("In which year were you born? "))
month = int(input("In which month were you born? "))
day = int(input("In which day were you born? "))
print("Birth date: " + str(day) + "/" + str(month) + "/" + str(year))

today = datetime.now()
print("Today: " + str(today.day) + "/" + str(today.month) + "/" + str(today.year))

age = today.year - year
if today.month < month or (today.month == month and today.day < day):
    age = age - 1

print("Your age is: " + str(age))
