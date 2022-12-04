import copy

def best(p, part2):
    fuel = float("inf")
    for i in range(len(p)): # for each possible position
        current_fuel = calc_fuel(p, i, part2)
        if current_fuel < fuel: # optimize fuel if possible
            fuel = current_fuel
    return(fuel)

def calc_fuel(positions, idx, part2):
    pos = copy.deepcopy(positions)
    fuel = 0
    x = pos.pop(idx) # get position to gather
    for i in pos:
        distance = abs(x-i)
        if part2:
            sum = 0
            for step in range(distance+1): 
                sum += step # p2 add series
            fuel += sum
        else: 
            fuel += distance # p1 add regular distance
    return fuel

with open('input.txt') as file:
    positions = [int(x) for x in file.read().rstrip().split(",")]
    print(best(positions, False), best(positions, True))

    