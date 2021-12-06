import copy

# import input
input = []
with open('input.txt') as text: 
    for line in text: 
        line = line.strip().split(" -> ")
        line[0] = [int(number) for number in line[0].split(",")]
        line[1] = [int(number) for number in line[1].split(",")]
        input.append(line)

#create empty tableau
def get_empty_tableau(lines):
    height = witdh = 0
    for line in lines:
        for coordinate in line:
            if coordinate[0]+1 > witdh: witdh = coordinate[0]+1
            elif coordinate[1]+1 > height: height = coordinate[1]+1
    tableau = [[0 for x in range(witdh)] for y in range(height)]
    return tableau

#help function
def print_tableau(tableau):
    print("Tableau:")
    for line in tableau:
        print(line)

#draw one line 
def draw_line(line, tableau):
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]: #not diagonal

        if line[0][1] == line[1][1]: # if same y --> horizontal
            length = abs(line[0][0] - line[1][0])+1
            starting_x = min(line[0][0], line[1][0])
            for i in range(length):
                #print("printing", starting_x+i, line[0][1])
                tableau[line[0][1]][starting_x+i] += 1
                #print("printed part", i+1)

        elif line[0][0] == line[1][0]: #-->vertical
            length = abs(line[0][1] - line[1][1])+1
            starting_y = min(line[0][1], line[1][1])
            for i in range(length):
                tableau[starting_y+i][line[0][0]] += 1

    elif diagonal(line):
        tableau = draw_diagonal(line, tableau)
    return tableau

#check if line is diagonal
def diagonal(line):
    length = abs(line[0][0] - line[1][0]) + 1
    step_x = step_y = 0 #determine steps (up or down)
    if line[0][0] < line[1][0]: step_x = 1
    else: step_x = -1
    if line[0][1] < line[1][1]: step_y = 1
    else: step_y = -1

    position = copy.deepcopy(line[0])
    for i in range(1, length):
        position[0] = position[0] + step_x
        position[1] = position[1] + step_y

    return position == line[1]

#outsourced
def draw_diagonal(line, tableau):
    length = abs(line[0][0] - line[1][0]) + 1

    step_x = step_y = 0
    if line[0][0] < line[1][0]: step_x = 1
    else: step_x = -1

    if line[0][1] < line[1][1]: step_y = 1
    else: step_y = -1

    for i in range(length):
        tableau[line[0][1] + i * step_y][line[0][0] + i * step_x] += 1
    return tableau

#main part
def draw_tableau(lines, tableau):
    for line in lines:
        tableau = draw_line(line, tableau)
    return tableau

#count zones with 2+ danger rating
def count_dagner_zones(tableau):
    counter = 0
    for row in tableau:
        for value in row:
            if value > 1:
                counter += 1
    return counter

tableau = draw_tableau(input, get_empty_tableau(input))
print(count_dagner_zones(tableau))