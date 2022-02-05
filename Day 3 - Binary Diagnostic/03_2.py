import copy           ### PART 2 ###

def search(list, most):                 # search for most or least common
    list = copy.deepcopy(list)          # deepcopy list to avoid manipulating the original
    for digit in range(len(list[0])):   # search bitwise
        criteria = criteria(list, digit, most)  # always recalculate criterion
        list = filter(list, digit, criteria)    # reduce list by criterion
    return list[0]

def criteria(list, y, most):     # most = 1 for oxygen (MSB)
    counter = 0                  # count ones 
    for x in range(len(list)):   
        if list[x][y] == 1: counter +=1
    if counter >= len(list)-counter: return most
    else: return not most

def filter(list, idx, check):
    i = 0
    while i < len(list):                       # while there remain unfiltered entries
        if len(list) == 1: return list
        if list[i][idx] != check: list.pop(i)  # pop if it does not meet criterion
        else: i+=1
    return list

def to_dec(bin):        # convert list of 
    result = 0          # binary integers to 
    print(len(bin))     # one decimal integer
    for i in range(len(bin)):
        result += bin[len(bin)-i-1] * 2**i
    return result

list = []
with open('input.txt') as input:
    for line in input:
        list.append([int(char) for char in line.strip()])

print(to_dec(search(list, 1)) * to_dec(search(list, 0)))