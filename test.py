#In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, 
#or dinner time. If it’s not time for a meal, don’t output anything at all. 
#Assume that the user’s input will be formatted in 
#24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive.
# For instance, whether it’s 7:00, 7:01,#7:59, or 8:00, or anytime in between, it’s time for breakfast.


from datetime import datetime


def convert_time(time):

    time = datetime.strptime(time, '%H:%M')

    return time


def main():
    time = input('What time is it? (HH:MM)')

    begin_breakfast_time = datetime.time(7,0)
    end_breakfast_time = datetime.time(8,0)
    begin_lunch_time = datetime.time(12,0)
    end_lunch_time = datetime.time(13,0)
    begin_dinner_time = datetime.time(18,0)
    end_dinner_time = datetime.time(19,0)
    
    time = convert_time(time) # chamando a funçao na main e pegando hour e minute


    if begin_breakfast_time < time < end_breakfast_time:
        return 'Breakfast Time'
    elif begin_lunch_time < time < end_lunch_time:
        return 'Lunch Time'
    elif begin_dinner_time < time < end_dinner_time:
        return 'Dinner Time'
    else:
        return 'Outside range'


if __name__ == '__main__':
    main()



# %%

#a = datetime.time(8,1)

datetime_object = datetime.datetime(2023, 2, 15, 8, 30)  # Example datetime object
time_part = datetime_object.time()  # Extract time part
print(time_part)  # Output: 08:30:00

# %%
