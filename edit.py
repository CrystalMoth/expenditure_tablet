# Houses all functions that are peforming and edit on a file (means editing a file's name, editing a row or creating one)
import file


#Module handels file row editing (meaning rm's aswell)

def edit_rows(file_name, lines):
    open(file_name, "w")
    print("\nEdit the line fully:\n")
    for row in lines:
        index = lines.index(row)
        print("Time period no.",index, row,"\n")
        modified_line = input()
        modified_line = f"{modified_line}\n"
        lines[index] = modified_line
    return lines



def edit_one_of_many(file_name):
    user_input = int(input("Choose a row number to edit it the row\n"))
    file = open(file_name)
    lines = file.readlines()  #Remember: user line - 1 = index
    index = user_input - 1
    print(lines[index])
    lines[index] = input("Edit the line fully: \n")
    lines[index] = f"{lines[index]}\n"
    
    open(file_name, "w")
    for i in lines:
        file.writelines(i)

    

def edit_one(file_name):
    file = open(file_name)
    one_line = file.readlines()
    print("Edit the line fully:\n", one_line, "\n")
    modified_line = input()
    modified_line = f"{modified_line}\n"
    one_line = modified_line
    return one_line






    
def rm_all(file_name):
    open(file_name, "w") # By opening the file, all of it's content's are removed. 