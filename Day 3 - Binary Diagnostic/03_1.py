list = []
with open('input.txt') as input:
    for line in input:
        list.append([int(char) for char in line.strip()])

def calc_rates(list, most):         # most = 1 for gamma (MSB)
    rate = []
    for y in range(len(list[0])):   # per digit
        counter = 0
        for x in range (len(list)): # count ones in all rows
            if list[x][y] == 1: counter += 1
        if counter >= len(list)-counter: rate.append(most)
        else: rate.append(int(not most))
    return rate

def to_dec(bin):        # convert list of 
    result = 0          # binary integers to 
    print(len(bin))     # one decimal integer
    for i in range(len(bin)):
        result += bin[len(bin)-i-1] * 2**i
    return result

print(to_dec(calc_rates(list, 1)) * to_dec(calc_rates(list, 0)))





