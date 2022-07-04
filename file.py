
def file_read(file_name):
    lines = []
    # Tries to open. (Add try-except later)
    file_r = open(file_name, "r")
    for file_row in file_r:
        file_row = file_row.strip()
        if not "#" in file_row: # All but #-rows pass
            lines.append(file_row)
    return lines

def file_write(file_name, lines):
    file = open(file_name, "a")
    for i in lines:
        file.writelines(i)


def pretty_column(rows):
    for i in range(len(rows)):
        print(f"{i + 1}. {rows[i]}")
