def worked_hours_for_now():
    pass


def worked_hours_for_today():
    pass


def show_the_tablet():

    pass

def update_salary():
    pass






def main():# Main() is for user input. Remember to use functions quite often so that for each new option, you can get quite far by simply combining functions
    print('''Hello. This is the WORK_TABLET

Please choose what you want to do by typing in the corresponding number and pressing eneter:

(1) Record the time worked until now (Finally a break. :))

(2) Record the time worked for today (Time to relax! :D)

(3) Display as a tablet the ammount of time worked (Time to be proud! ;))

(4) Update the salary (So you are growing to become a professional? :))
     ''')


user_input = input()
if user_input == 1:
    worked_hours_for_now()
elif user_input == 2:
    worked_hours_for_today()
elif user_input == 3:
    show_the_tablet()
elif user_input == 4:
    update_salary()
else:
    






main()