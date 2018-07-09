# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

#var name
user_name = raw_input("What is your name? ")
# user_grade = raw_input("What grade are you in? ")
# user_years = 12 - int(user_grade)
#
# #display years
# if int(user_years) == 1:
#     print user_name + ", you will graduate in", (user_years), "year."
# elif int(user_years) == 0:
#     print user_name + ", you will graduate this year."
# elif int(user_years) < 0:
#     print user_name + ", you have already graduated."
# elif int(user_years) > 11:
#     print user_name + ", that is not a real grade!"
# else:
#     print user_name + ", you will graduate in", (user_years), "years."



# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday

#var name
user_bmonth = raw_input("What is your month of birth? ")
user_bday = raw_input("What is your day of birth? ")
current_month = 7
current_day = 9

#define month and day distance
if int(user_bmonth) >= current_month and int(user_bday) >= current_day:
    month_distance = int(user_bmonth) - current_month
    day_distance = int(user_bday) - current_day
elif int(user_bmonth) >= current_month and int(user_bday) < current_day:
    if int(user_bmonth) == current_month:
        month_distance = 11
        day_distance = 30-current_day+int(user_bday)
    else:
        month_distance = int(user_bmonth) - current_month - 1
        day_distance = 30-current_day+int(user_bday)
elif int(user_bmonth) < current_month and int(user_bday) >= current_day:
    month_distance = 12 - current_month+int(user_bmonth)
    day_distance = int(user_bday) - current_day
else:
    month_distance = 11 - current_month + int(user_bmonth)
    day_distance = 29-current_day+int(user_bday)

#check for bday
if int(user_bmonth) == current_month and int(user_bday) == current_day:
    bday = True
else:
    bday = False

#print message
if bday == False:
    print user_name, ", your birthday is in", month_distance, "months and", day_distance, "days."
else:
    print "Happy birthday,", user_name, "!"


# If you complete extensions, describe your extensions here!


