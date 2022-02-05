input = []
with open('input.txt') as text: 
    for line in text: input.append(int(line.strip()))
def count_increases(input, distance):
    counter = 0
    for i in range(0, len(input)-distance):
        if input[i+distance] > input[i]: counter += 1
    return counter
print("Results:", count_increases(input, 1), count_increases(input, 3))