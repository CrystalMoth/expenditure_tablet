# Houses all functions that are peforming and edit on a file (means editing a file's name, editing a row or creating one)
def edit_all(file_name):
    file = open(file_name)
    lines = file.readlines()
    open(file_name, "w")
    open(file_name, "a")
    print("\nEdit the line work period fully:\n")
    for row in lines:
        index = lines.index(row)
        print(row,"\n")
        modified_line = input()
        modified_line = f"{modified_line}\n"
        lines[index] = modified_line
    file = open(file_name, "w")
    file.writelines(lines)    
    



def edit_one():
    pass    

def rm_all():
    open(TEMP_FILE_NAME, "w") # By opening the file, all of it's content's are removed. 
edit_all(TEMP_FILE_NAME)