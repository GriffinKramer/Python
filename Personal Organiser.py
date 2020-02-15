'''
Griffin Kramer
3rd Comp Science
4/23/19
Personal Organiser
'''

def append_to_arrays(Day, Month, Year, Name, day_of_event, month_of_event, year_of_event, name_of_event):
    Year.append(year_of_event)
    Name.append(name_of_event)
    Day.append(day_of_event)
    Month.append(month_of_event)


def fix_day(month_of_event, day_of_event):
    if month_of_event in [1, 3, 5, 7, 8, 10, 12]:
        if day_of_event > 31 or day_of_event < 1:
            day_of_event = 1

    if month_of_event in [4, 6, 9, 11]:
        if day_of_event > 30 or day_of_event < 1:
            day_of_event = 1

    if month_of_event == 2:
        if day_of_event > 28 or day_of_event < 1:
            day_of_event = 1

    return day_of_event


def add_event(Day, Month, Year, Name):

    loop = True

    while loop == True:
    
        name_of_event = input('What is the event: ')
        month_of_event = int(input('What is the month (number): '))
        day_of_event = int(input('What is the date: '))
        year_of_event = int(input('What is the year: '))

        if month_of_event < 1 or month_of_event > 12:
            month_of_event = 1

        day_of_event = fix_day(month_of_event, day_of_event)

        append_to_arrays(Day, Month, Year, Name, day_of_event, month_of_event, year_of_event, name_of_event)

        continu = input('Do you want to enter another date?')

        if continu.lower() == 'no':
            loop = False


def print_event(i, Name, Month_of_event, Day, Year):

    print(Name[i])
    print('Date: ' + Month_of_event + ' ' + str(Day[i]) + ', ' + str(Year[i]))

        
def list_of_events(Day, Month, Year, Name):
    print('******************** List of Events ********************')
    
    months_in_year = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for i in range (len(Day)):

        Months = Month[i]
        Month_of_event = months_in_year[Months - 1]
        print_event(i, Name, Month_of_event, Day, Year)
    
        
def events_in_month(Day, Month, Year, Name):

    months_in_year = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    what_month = int(input('What month would you like to see?(Enter the month number)'))
    
    print('********** Events in ' + months_in_year[what_month -1] + ' **********' )  
        
    for i in range (len(Month)):

        Months = Month[i]
        Month_of_event = months_in_year[Months - 1]
        
        if what_month == Month[i]:
            print_event(i, Name, Month_of_event, Day, Year) 
    
   
Names = []
Years = []
Months = []
Days = []
add_event(Days, Months, Years, Names)
list_of_events(Days, Months, Years, Names)
events_in_month(Days, Months, Years, Names)
