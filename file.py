
#Module Handels file reading/writing


def file_read(file_name):
    lines = []
    # Tries to open. (Add try-except later)
    file_r = open(file_name)
    for file_row in file_r:
        file_row = file_row.strip()
        if not "#" in file_row: # All but #-rows pass
            if file_row != None:
                lines.append(file_row)
    print(lines, "lol")
    return lines

def file_write(file_name, lines):
    file = open(file_name, "a")
    for i in lines:
        file.writelines(i)




