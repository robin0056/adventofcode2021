import copy

# import input
input = []
with open('input.txt') as text: 
    for line in text: input.append(line.strip())

# small help function
def print_tableaus(tableaus): 
    for tableau in tableaus:
        for line in tableau:
            print(line)
        print("")

# extract sequence
def get_sequence(input):
    sequence = input[0].strip().split(",")
    sequence = [int(number) for number in sequence]
    return sequence

#mark number if match 
#marked numbers wont be
#considered when calculating 
#the sum for the result
def mark(tableau, draw):
    for x in range(5):
        for y in range(5):
            if tableau[x][y] == draw:   #if match
                tableau[x][y] = -1      #mark number
    return tableau

# get list of tableaus
def get_tableaus(input):
    input = copy.deepcopy(input)
    #clean first two lines 
    input.pop(0)
    input.pop(0)
    for line in input: #and empty lines
        if line == "":
            input.pop(input.index(""))
    #create small tableaus
    tableaus = []
    for i in range(int(len(input)/5)):      #per tableau
        tmp_tableau = []                    #create list
        for i in range(5):                  #per line
            line = input.pop(0).split(" ")  #split between spaces
            for item in line:
                if item == "":              #in case there are double spaces
                    line.pop(line.index(""))
            line = [int(number) for number in line]   #cast numbers to int
            tmp_tableau.append(line) #add line
        tableaus.append(tmp_tableau) #add tableau
    return tableaus

def calc_tableau_sum(tableau):
    sum = 0
    for row in range(len(tableau)):
        for column in range(len(tableau[row])):
            if tableau[row][column] != -1: sum += tableau[row][column]
    return sum

def calc_result(tableau, draw):
    return "score:", calc_tableau_sum(tableau) * draw

def check_for_win(tableau):
    #check row
    for row in tableau:
        no_marked = 0
        for number in row:
            if number == -1: no_marked += 1
        if no_marked == 5: return True

    # check columns
    for column in range(5):
        no_marked = 0
        for row in range(5):
            if tableau[row][column] == -1: no_marked += 1
        if no_marked == 5: return True

    return False # player did not win yet

#### PART ONE ####
def play_bingo(input):
    sequence = get_sequence(input)
    tableaus = get_tableaus(input)
    for draw in sequence:
        for player in range(len(tableaus)):
            tableaus[player] = mark(tableaus[player], draw)
            if check_for_win(tableaus[player]): 
                return calc_result(tableaus[player], draw)

#### PART TWO ####
def play_but_loose(input):

    sequence = get_sequence(input)      # get basic 
    tableaus = get_tableaus(input)      # game elements

    for draw in sequence:
        for tableau in tableaus:            # for all players
            tableau = mark(tableau, draw)   # mark if match 

        for tableau in tableaus:
            if len(tableaus) == 1 & check_for_win(tableau):  # if last
                return calc_result(tableau, draw)            # one wins
            elif check_for_win(tableau): 
                tableaus.pop(tableaus.index(tableau))        # no winners here

print(play_bingo(input))
print(play_but_loose(input))




