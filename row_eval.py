from ast import Import
from http.client import ImproperConnectionState
import imp
import edit
from constants import*
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