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




def more_than_one(rows):
    file.pretty_column(rows)
    print('''\nMultiple rows have been recorded. Would you like to do one of the following?:\n
(1) Edit all of the rows
(2) edit a spesific row 
(3) Remove all of the rows''')
    user_input = int(input())
    if user_input == 1:
        rows = file.file_read(TEMP_FILE_NAME)
        rows = edit.edit_rows(TEMP_FILE_NAME, rows)
        file.file_write(TEMP_FILE_NAME, rows)
        file.file_write(REC_FILE_NAME, rows)
        edit.rm_all(TEMP_FILE_NAME)
        print("Time periods have been stored")
        sleep(2)
        main()

    elif user_input == 2:
        file.pretty_column(rows)
        edit.edit_one(TEMP_FILE_NAME)
    else:
        edit.rm_all(TEMP_FILE_NAME)


def only_one(rows):
    pass


def no_rows():
    print("No rows detected. Returning to main menu")
    sleep(2)



def edit_work_time(): #Let's user input the time worked and saves it in a file containing temporary data to be moved elsewhere later (for_today-function)
    # Should look for temp_work_file and asks what the user wants to do with it. (add, remove, update)

    # Tells the user what day it is. (In case being used in the terminal and it is importan information)
    todays_date = datetime.now()
    print("\nToday it is {}.{}.{}\n".format(str(todays_date.day), str(todays_date.month), str(todays_date.year)))
    row_temp_rows = file.file_read(TEMP_FILE_NAME)
    if len(row_temp_rows) >= 2: # If temp_file has more than 2 rows
        more_than_one(row_temp_rows)
    elif len(row_temp_rows) == 1:
        only_one(row_temp_rows)
    else:
        no_rows()
    

def rec_work_time():
    pass


def show_the_tablet():

    pass

def update_salary():
    pass



def main(): # This loop is the main if-clause. When error occurs or something alike, return to this loop

    print('''Type the corresponding number:

    (1) Record the time worked

    (2) edit the time worked for

    (3) Display as a tablet the ammount of time worked

    (4) Update the salary

    (5) Quit''')

    try:
        user_input = int(input())
        if user_input == 1:
            rec_work_time()
        elif user_input == 2:
            edit_work_time()
        elif user_input == 3:
            show_the_tablet()
        elif user_input == 4:
            update_salary()
        elif user_input == 5:
            exit()
        else:
            print("Invalid number. Moving to main menu\n")
            sleep(3)
            main()
    except ValueError:
        print("Not a number. Moving to main menu\n")
        sleep(3)
        main()
        

#Start print
print("Hello. This is the WORK_TABLET")
main()