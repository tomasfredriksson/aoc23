import re

testfile = open("testdata/2a.txt", "r")
inputfile = open("inputdata/2a.txt", "r")

#boundaries are [red, green, blue]
boundaries = [12, 13, 14]
lines = inputfile.readlines()
ok_ids = []
all_power_balls = []
for line in lines:
    splitted_line = re.split('; |:', line)
    id = splitted_line[0].strip('Game ')
    dirty_sets = []
    for i in range(len(splitted_line)-1):
        dirty_sets.append(splitted_line[i+1].strip('\n '))
    sets = []
    for j in range(len(dirty_sets)):
        subset = dirty_sets[j].split(',')
        sorted_subset = [0, 0, 0]
        for color in subset:
            if 'red' in color:
                sorted_subset[0] = int(color.strip(' red '))
            if 'green' in color:
                sorted_subset[1] = int(color.strip(' green '))
            if 'blue' in color:
                sorted_subset[2] = int(color.strip(' blue '))
        sets.append(sorted_subset)
    #part 2
    #print("new set:")
    max_balls = [0, 0, 0]
    for set in sets:
        if set[0] > max_balls[0]:
            max_balls[0] = set[0]
        if set[1] > max_balls[1]:
            max_balls[1] = set[1]
        if set[2] > max_balls[2]:
            max_balls[2] = set[2]
    power_balls = max_balls[0]*max_balls[1]*max_balls[2]
    allisfine=True
    for set in sets:
        if set[0] > boundaries[0]:
            allisfine=False
        if set[1] > boundaries[1]:
            allisfine=False
        if set[2] > boundaries[2]:
            allisfine=False
    if allisfine:
        ok_ids.append(id)
    all_power_balls.append(power_balls)
    #print(id, power_balls)
sum = 0
for ids in ok_ids:
    sum += int(ids)
print("part1: ", sum)
ballsum = 0
for balls in all_power_balls:
    ballsum += balls
print("part2:", ballsum)