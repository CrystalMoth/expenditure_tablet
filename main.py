import printz
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

#Main program

def back_to_menu():
    print("Returning to main menu")
    sleep(1.5)
    main()    


def more_than_one(rows):
    printz.pretty_column(rows)
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
        print("Time periods have been stored\n")
        back_to_menu()
 
    elif user_input == 2:
        printz.pretty_column(rows)
        edit.edit_one(TEMP_FILE_NAME)
    else:
        edit.rm_all(TEMP_FILE_NAME)


def only_one(rows):
    print("Only one row found:\n")
    printz.pretty_column(rows)
    user_input = int(input("\nPress 'Y' to edit.\n"))
    if user_input == "y":
        edit.edit_one()
    else:
        back_to_menu()
    


def no_rows():
    print("No rows detected\n")
    back_to_menu()

def edit_work_time(): #Let's user input the time worked and saves it in a file containing temporary data to be moved elsewhere later (for_today-function)

    # Tells the user what day it is. (In case being used in the terminal and it is importan information)
    print("Today it is", printz.show_date())
    temp_rows = file.file_read(TEMP_FILE_NAME)
    if len(temp_rows) >= 2:
        more_than_one(temp_rows)
    elif len(temp_rows) == 1:
        only_one(temp_rows)
    else:
        no_rows()
    

def rec_work_time():
    print('''How to record your time:
    write "-" for a period of time you want to record. Example: 12-13
    If you have multiple periods use ":". Example: 12-30: 14-15.20''')    


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
            print("Invalid number.\n")
            back_to_menu()
    except ValueError:
        print("Not a number.\n")
        back_to_menu()
        

#Start print
print("Hello. This is the WORK_TABLET")
main()