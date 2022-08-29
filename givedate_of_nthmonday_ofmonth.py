import datetime

'''
weekday:
0 = Monday
1 = Tuesday
.
.
.
6 = Sunday
'''

def give_the_date_of_the_nth_day_of_the_month(year,month,weekday,nth):
    first_date_of_the_month = datetime.date(year,month,1)
    offset = weekday - first_date_of_the_month.weekday()
    if(offset < 0):
        offset += 7
    target_date = first_date_of_the_month + datetime.timedelta(offset + (nth - 1) * 7)
    return target_date

#Date of the first Monday in October 2022
give_the_date_of_the_nth_day_of_the_month(2022,10,0,1)

#Date of the 3rd Saturday in April 2021
give_the_date_of_the_nth_day_of_the_month(2021,4,5,3)