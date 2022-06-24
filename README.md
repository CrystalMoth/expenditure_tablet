The WORK_TABLET let's the user keep a record of their working ours per day/week and month as well as the salary they will/would habe earned based on the inputs given

The WORK_TABLET gives the user a list of options and the user chooses how they will proceed

Examples of this might include: The Ability to add, remove and update working hours, update given salary, display a complete view of work done and/or salary earned

    Goal(s): 
        The core of the program is to keep track of working hours

        The program has to be able handle many types of minute to hour convertions

        The user should NEVER be confused about what the program is executing, asking and displaying

        The language used has to be 100 % Python


        
Repo nav:

WORK_TABLET repo is made out of 4 files: main program (main), temp_work, rec_work and README

Main program ()(work_tablet.py) does r/w to temp_work and rec_work

Functionality:

temp_work stores work that does not yet cover all the work for the day (for an example: The user is taking a break or simply not working)

r:temp_work: Program reads from the file, displays the necesery information (narrows with user input) and ask the user of an action (update, remove or add)

w:temp_work: After the user has asked for an action, main writes into (most likely) a row

r:rec_work: If the user asks for the full view of their work, main reads from this file and prints what the user asks for (monthly work, salary per week etc.)

w:rec_work: If the user chooses an option that implicates a days/weeks etc. work being done, main writes that information into the file (format is yet unkown)





