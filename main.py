from calendar import weekday
from datetime import datetime
from multiprocessing.spawn import old_main_modules
from posixpath import split
import edit
from matplotlib.pyplot import close
from constants import*
#Constants. DO NOT CHANGE THE FILE NAMES

# Global variables
row_s = [] 

def temp_work_r():
    # Tries to open. (Add try-except later)
    file_r = open(TEMP_FILE_NAME, "r")
    for file_row in file_r:
        file_row = file_row.strip()
        if not "#" in file_row: # All but #-rows pass. Other row-excluding symbols may be added in the future...
            row_s.append(file_row)
    return row_s

    




def more_than_one(row_s):
    for i in range(len(row_s)):
        print(f"{i + 1}. {row_s[i]}")
    print('''\nMultiple rows have been recorded. Would you like to do one of the following?:\n
(1) Edit all of the rows
(2) edit a spesific rowindex
(3) Remove all of the rows''')
    user_input = int(input())
    if user_input == 1:
        edit.edit_all()
    elif user_input == 2:
        edit.edit_one()
    else:
        edit.rm_all()

def only_one(row_s):
  pass


def no_rows():
    pass




def worked_hours_for_now(): #Let's the user input the time worked and saves it in a file which contains temporary data to be moved elsewhere later (for_today-function)
    # Should look for temp_work_file and asks what the user wants to do with it. (add, remove, update)

    # Tells the user what day it is. (In case being used in the terminal and it is importan information)
    todays_date = datetime.now()
    print("\nToday it is {}.{}.{}\n".format(str(todays_date.day), str(todays_date.month), str(todays_date.year)))
    row_s = temp_work_r()
    print(row_s)
    if len(row_s) >= 2: # If temp_file has more than 2 rows, the user should want to view, make hanges, or remove.
        more_than_one(row_s)
    elif len(row_s) == 1:
        only_one(row_s)
    else:
        no_rows()
    

def worked_hours_for_today():
    pass


def show_the_tablet():

    pass

def update_salary():
    pass





def main():# Main() is for user input. Remember to use functions quite often so that for each new option, you can get quite far by simply combining functions

    #Start print
    print('''Hello. This is the WORK_TABLET

Please choose what you want to do:

(1) Record the time worked until now (Finally a break. :))

(2) Record the time worked for today (Time to relax! :D)

(3) Display as a tablet the ammount of time worked (Time to be proud! ;))

(4) Update the salary (So you are growing to become a professional? :))
    ''')

    #Directing the user's wish to a function
    user_input = int(input("Type the corresponding number: \n"))
    if user_input == 1:
        worked_hours_for_now()
    elif user_input == 2:
        worked_hours_for_today()
    elif user_input == 3:
        show_the_tablet()
    elif user_input == 4:
        update_salary()
    else:
        print("Something went wrong")
main()