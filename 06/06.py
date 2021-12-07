import copy

def simulate(population, days):
    p = [] # p[x] stores how many fish exist with value x

    for i in range(9): # for each possible fish value
        counter = 0
        for fish in population: # count its instances
            if i == fish: counter += 1
        p.append(counter)

    for day in range(days): # simulate
        tmp = copy.deepcopy(p)
        for j in range(len(p)):
            p[j-1] = tmp[j] # let fishes age
        p[6] += tmp[0] # reset value if it was 0

    return sum(p)

with open('input.txt') as file:
    population = [int(x) for x in file.read().rstrip().split(",")]
    print(simulate(population, 80), simulate(population, 256))

    