list = []
with open('input.txt') as input:    # import input
    for line in input:              # as list
        list.append(str(line.strip()).split(" "))

def calc_position(list, is_first_subtask):
    x = z = aim = 0
    for item in list:                               # iterate instruction list
        if item[0] == "forward": x += int(item[1])  # always go forward
        if is_first_subtask:
            if item[0] == "up": z -= int(item[1])       # calc depth according
            if item[0] == "down": z += int(item[1])     # to first task
        else:
            if item[0] == "forward": z += aim * int(item[1]) # calc depth and
            if item[0] == "up": aim -= int(item[1])          # aim according to 
            if item[0] == "down": aim += int(item[1])        # second task
    return x * z

print("Results:", calc_position(list, 1), calc_position(list, 0))