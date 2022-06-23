from calendar import weekday
from datetime import datetime
from posixpath import split
#Constants. DO NOT CHANGE THE FILE NAMES
TEMP_FILE_NAME = "temp_work.txt"
REC_FILE_NAME = "rec_work.txt"
ROW_SKIP_COND = '#'

# Global variables
row_s = [] 

def temp_work_r():
    # Tries to open. (Add try-except later)
    file_r = open(TEMP_FILE_NAME, "r")
    for file_row in file_r:
        file_row = file_row.strip()
        if not "#" in file_row: # All but #-rows pass. Other row-excluding symbols may be added in the future...
            row_s.append(file_row)
    print(row_s)




def worked_hours_for_now(): #Let's the user input the time worked and saves it in a file which contains temporary data to be moved elsewhere later (for_today-function)
    # Should look for temp_work_file and asks what the user wants to do with it. (add, remove, update)

    # Tells the user what day it is. (In case being used in the terminal and it is importan information)
    todays_date = datetime.now()
    print("\nToday it is {}.{}.{}\n".format(str(todays_date.day), str(todays_date.month), str(todays_date.year)))
    row_s = temp_work_r()
            

    

    



    

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