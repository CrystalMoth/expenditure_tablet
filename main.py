from calendar import weekday
from datetime import datetime
from multiprocessing.spawn import old_main_modules
from posixpath import split
from time import sleep
import file
import edit
from matplotlib.pyplot import close
# This file houses all constants and possibly other variables that are going to be used in multiple modules
TEMP_FILE_NAME = "temp_work.txt"
REC_FILE_NAME = "rec_work.txt"
ROW_SKIP_COND = '#'

# Global variable. Reason: row_s is an important var and it is used often and in many places. Viewing it as global makes it easier to understand it's role in the code
row_s = [] 





def more_than_one(row_s):
    for i in range(len(row_s)):
        print(f"{i + 1}. {row_s[i]}")
    print('''\nMultiple rows have been recorded. Would you like to do one of the following?:\n
(1) Edit all of the rows
(2) edit a spesific row
(3) Remove all of the rows''')
    user_input = int(input())
    if user_input == 1:
        edit.edit_all(TEMP_FILE_NAME)
        user_input = input("Press 'y' to store the work period")
        if user_input == "y":
            file.file_write(REC_FILE_NAME, row_s)
            edit.rm_all(TEMP_FILE_NAME)

    elif user_input == 2:
        user_input = input("Do you want to move all of the ")
        edit.edit_one(TEMP_FILE_NAME)
    else:
        edit.rm_all(TEMP_FILE_NAME)


def only_one(row_s):
    pass


def no_rows():
    pass



def worked_hours_temp(): #Let's user input the time worked and saves it in a file containing temporary data to be moved elsewhere later (for_today-function)
    # Should look for temp_work_file and asks what the user wants to do with it. (add, remove, update)

    # Tells the user what day it is. (In case being used in the terminal and it is importan information)
    todays_date = datetime.now()
    print("\nToday it is {}.{}.{}\n".format(str(todays_date.day), str(todays_date.month), str(todays_date.year)))
    row_s = file.file_read(TEMP_FILE_NAME)
    if len(row_s) >= 2: # If temp_file has more than 2 rows, the user should want to view, make canges, or remove.
        more_than_one(row_s)
    elif len(row_s) == 1:
        only_one(row_s)
    else:
        no_rows()
    

def worked_hours_rec():
    pass


def show_the_tablet():

    pass

def update_salary():
    pass



def main_loop():
    print("Type the corresponding number:")
    try:
        user_input = int(input())
        if user_input == 1:
            worked_hours_temp()
        elif user_input == 2:
            worked_hours_rec()
        elif user_input == 3:
            show_the_tablet()
        elif user_input == 4:
            update_salary()
        else:
            print("Invalid number. the program closes")
            sleep(3)
            exit()
    except ValueError:
        print("Not a number. The program closes")
        sleep(3)
        exit()
        

def main():# main() is for user input. Remember to use functions quite often so that for each new option, you can get quite far by simply combining functions

    #Start print
    print('''Hello. This is the WORK_TABLET

Please choose what you want to do:

(1) Record the time worked until now

(2) Record the time worked for today

(3) Display as a tablet the ammount of time worked

(4) Update the salary
    ''')
    main_loop()

main()