from multiprocessing.connection import answer_challenge
import printz
from multiprocessing.spawn import old_main_modules
from posixpath import split
from time import sleep
import file
import edit
from matplotlib.pyplot import close

# This file houses all constants and possibly other variables that are going to be used in multiple modules
EXPENSE_FILE = "expenses.txt"
ROW_SKIP_COND = '#'

#Main program
def back_to_menu():
    print("Returning to main menu")
    sleep(3)
    main()    


def more_than_one(rows):
    printz.pretty_column(rows)
    print('''\nMultiple rows have been recorded. Would you like to do one of the following?:\n
(1) Edit all of the rows
(2) edit a spesific row 
(3) Remove all of the rows''')
    user_input = int(input())
    if user_input == 1:
        rows = file.file_read(EXPENSE_FILE)
        rows = edit.edit_rows(EXPENSE_FILE, rows)
        file.file_write(EXPENSE_FILE, rows)
        file.file_write(EXPENSE_FILE, rows)
        edit.rm_all(EXPENSE_FILE)
        print("Time periods have been stored\n")
        back_to_menu()

    elif user_input == 2:
        printz.pretty_column(rows)
        edit.edit_one_of_many(EXPENSE_FILE)
    else:
        edit.rm_all(EXPENSE_FILE)


def only_one(rows):
    print("Only one row found:\n")
    printz.pretty_column(rows)
    user_input = input("\nPress 'Y' to edit.\n")
    if user_input == "y":
        edit.edit_one(EXPENSE_FILE)
        print("Line edited succesfully\n")
        back_to_menu()

    else:
        back_to_menu()
    


def no_rows():
    print("\nNo rows detected\n")
    back_to_menu()

def edit_expenses(): #Let's user input the time worked and saves it in a file containing temporary data to be moved elsewhere later (for_today-function)

    # Tells the user what day it is. (In case being used in the terminal and it is importan information)
    print("Today it is", printz.show_date())
    temp_rows = file.file_read(EXPENSE_FILE)
    if len(temp_rows) >= 2:
        more_than_one(temp_rows)
    elif len(temp_rows) == 1:
        only_one(temp_rows)
    else:
        no_rows()
    

def rec_expenses():
    user_input = input('''Write the name of the expense and the monthly pay seperated by (:) Note: Use Euros.
    IF you want to write multipel expenses, simply seperate them by using comma  and a space (, )
    Example: My_expense:12.5, another_one:7.25\n''')
    file.file_write(EXPENSE_FILE, user_input)
    print("Expenditures have been recorded\n")
    back_to_menu()


def show_the_table():
    printz.pretty_column(file.file_read(EXPENSE_FILE))
    back_to_menu()
    pass

def update_budget():
    pass



def main(): # This loop is the main if-clause. When error occurs or something alike, return to this loop

    print('''Type the corresponding number:

    (1) Record the time worked

    (2) edit the expenditure(s)

    (3) Display all the expenditures

    (4) Update budget

    (5) Quit''')

    try:
        user_input = int(input())
        if user_input == 1:
            rec_expenses()
        elif user_input == 2:
            edit_expenses()
        elif user_input == 3:
            show_the_table()
        elif user_input == 4:
            update_budget()
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