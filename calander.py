'''
Calander
Griffin Kramer
3/7/2019
3rd Period CS
'''

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
         return 0


def number_of_days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if leap_year(year) == 1:
            return 29
        else:
            return 28

def days_left(year, month, day):
    days_left = 0
    for i in range (month + 1, 13):
        days_left = days_left + number_of_days(year, i)
    day_add = number_of_days(year, month) - day
    return days_left + day_add

day = int(input("Please enter the day: "))
month = int(input("Please enter the month: "))    
year = int(input("Please enter the year: "))
menu = int(input("Menu\n1 for days in month\n2 for days left in year\n0 to stop: "))
while menu != 0:
    if menu == 1:
        print(number_of_days(year, month))
    elif menu == 2:    
        print(days_left(year, month, day))
    menu = int(input("Menu\n1 for days in month\n2 for days left in year\n0 to stop loop: "))  


