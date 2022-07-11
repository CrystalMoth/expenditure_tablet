from calendar import weekday
from datetime import datetime
from time import sleep
#Module handles repetitive printing and simple commands related to the printing

def pretty_column(rows):
    print("\n")
    for i in range(len(rows)):
        print(f"{i + 1}. {rows[i]}")


        
def show_date():
    todays_date = datetime.now()
    return f"{str(todays_date.day)}.{str(todays_date.month)}.{str(todays_date.year)}"
