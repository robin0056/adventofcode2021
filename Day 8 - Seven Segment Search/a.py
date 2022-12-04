def get_input() -> list:
    with open(r'input.txt', 'r') as file:
        file_list = file.read().splitlines()
    file_list = [i.split() for i in file_list]
    return file_list

def partOne(digits):
    cnt = 0
    for clock in digits:
        for num in clock[-4:]:
            if len(num) in [2,4,3,7]:
                cnt += 1
    return cnt

def partTwo(digits):
    num_list = [[sorted([k for k in j]) for j in i if j != '|']for i in digits]
    num_sum = 0
    print(num_list)
    for i in num_list:
        lookup = id_digits(i[:-4])
        number = ''
        for j in i[-4:]:
            number += str(lookup[tuple(j)])
        num_sum += int(number)
        print(number)
    return num_sum

def id_digits(dig_list):
    dig_lookup = dict()
    # fill known numbers 1,7,4,8
    for i in dig_list:
        num_seg = len(i)
        if num_seg == 2:
            dig_lookup[tuple(i)] = 1
            dig_lookup[1] = i
        elif num_seg == 3:
            dig_lookup[tuple(i)] = 7
            dig_lookup[7] = i
        elif num_seg == 4:
            dig_lookup[tuple(i)] = 4
            dig_lookup[4] = i
        elif num_seg == 7:
            dig_lookup[tuple(i)] = 8
            dig_lookup[8] = i
    five_seg = [i for i in dig_list if len(i) == 5]
    six_seg = [i for i in dig_list if len(i) == 6]
    for i in six_seg:
        if not(dig_lookup[1][0] in i and dig_lookup[1][1] in i):
            # fill 6
            dig_lookup[tuple(i)] = 6
            dig_lookup[6] = i
            # find segments c and f
            if dig_lookup[1][0] not in i:
                seg_c = dig_lookup[1][0]
                seg_f = dig_lookup[1][1]
            else:
                seg_c = dig_lookup[1][1]
                seg_f = dig_lookup[1][0]
    for i in five_seg:
        # fill numbers 2,5,3
        if seg_f not in i:
            dig_lookup[tuple(i)] = 2
            dig_lookup[2] = i
        if seg_c not in i:
            dig_lookup[tuple(i)] = 5
            dig_lookup[5] = i
        if seg_f in i and seg_c in i:
            dig_lookup[tuple(i)] = 3
            dig_lookup[3] = i
    # fill number 9
    dig_lookup[9] = sorted(dig_lookup[5] + [seg_c])
    dig_lookup[tuple(sorted(dig_lookup[5] + [seg_c]))] = 9
    for i in six_seg:
        if not(tuple(i) in dig_lookup.keys()):
            dig_lookup[tuple(i)] = 0
            dig_lookup[0] = i
    return dig_lookup

def main():
    digits = get_input()
    print(f"The answer to part 1 is {partOne(digits)}")
    print(f"The answer to part 2 is {partTwo(digits)}")

if __name__ == '__main__':
    main()