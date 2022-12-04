import copy

#### OPEN AND CLEAN INPUT ####
def open_input():
    with open('input.txt') as file:
        lines = [[x.split()] for x in file.readlines()]
        # put last 4 digits into seperate list and remove "|"
        for line in lines:
            line.append([line[0].pop(-1) for i in range(4)]) 
            line[0].pop(-1)
    return lines

#### PART 1 ####
def count_uniques(lines):
    counter = 0
    unique_segments = [2,3,4,7] # for numbers 1, 4, 7, 8
    for line in lines:
        for digit in line[1]:
            if len(digit) in unique_segments:
                counter += 1
    return counter

def reconnect_wires(line):
    all_segments = set("abcdefg")

    references = [-1 for i in range(10)]
    references[1] = find(line[0], 2)
    references[4] = find(line[0], 4)
    references[7] = find(line[0], 3)
    references[8] = find(line[0], 7)

    print(line)
    print(references)
    print("")

    # 0, 6, 9 use all except of one segment
    # the unsused segment of 6 appears in 1
    # the unsused segment of 0 appears in 4
    pot = [find(line[0], 6) for i in range(3)] # potential candidates for 0, 6, 9
    ex = [list(set(pot[i]).symmetric_difference(all_segments))[0] for i in range(3)]
    print(pot, ex)
    done = []
    for i in range(3):
        if ex[i] in references[1]: 
            references[6] = pot[i]
            print("added 6:" , pot[i])
            done.append(i)
        if ex[i] in references[4]:
            print("added 0:", ex[i] , pot[i])
            references[0] = pot[i]
            done.append(i)
    idx_nine = list(set([0,1,2]).symmetric_difference(set(done)))[0]
    references[9] = pot[idx_nine]
    print(line)
    print(references)
    print("")



    # 2, 3 and 5 each have 5 segments
    # the unused segments of 3 cannot be found in 1








def find(digits, no_segments):
    for i in range(len(digits)):
        if len(digits[i]) == no_segments:
            return digits.pop(i)

input = open_input()
reconnect_wires(input[1])
#print(count_uniques(input)) # part 1

