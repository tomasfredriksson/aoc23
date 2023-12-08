def main():
    testfile = open("testdata/3a.txt", "r")
    inputfile = open("inputdata/3a.txt", "r")
    lines = testfile.readlines()

    map = []
    for line in lines:
        sorted_lines = line.strip('\n')
        map_part = []
        for c in sorted_lines:
            map_part.append(c)
        map.append(map_part)
        print(map_part)

    # Find Numbers
    accNumList = []
    decNumList = []
    gearNumList = []
    y_width = len(map)
    x_width = len(map[0])
    for y in range(y_width):
        for x in range(x_width):
            if map[y][x].isdigit():
                num, status, gear = checkAround(map, y, x, y_width, x_width)
                if int(num) < 1000:
                    if status:
                        if gear:
                            gearNumList.append(num)
                        else:
                            accNumList.append(num)
                    else:
                        decNumList.append(num)
                else:
                    print("Hmm...", num, x, y)
    #print("Accepted: ", accNumList)
    #print("Declined: ", decNumList)
    #for mapP in map:
        #print(mapP)
    serialSum = 0
    for serialNumber in accNumList:
        serialSum += int(serialNumber)
    print(serialSum)
    print(gearNumList)

def checkAround(map, y, x, y_width, x_width):
    # Find the full number
    # Check to the right
    valid = False
    gear = False
    number = ''
    for i in range(x,x_width,1):
        if map[y][i].isdigit():
            number = number + map[y][i]
            valid = surroundings(map, valid, y, i)
            map[y][i] = '.'
        else:
            if map[y][i] == '*':
                gear = True
            break
    for j in range(x-1,-1,-1):
        if map[y][j].isdigit():
            number = map[y][j] + number
            valid = surroundings(map, valid, y, j)
            map[y][j] = '.'
        else:
            if map[y][j] == '*':
                gear = True
            break
    return number, valid, gear

def surroundings(map, valid, y, x):
    symbols = ['@', '#', '$', '%', '&', '*', '/', '+', '-', '=']
    x_bound_s = x-1
    if x == 0:
        x_bound_s = 0
    x_bound_e = x+1
    if x == len(map[y])-1:
        x_bound_e = x
    y_bound_s = y-1
    if y == 0:
        y_bound_s = 0
    y_bound_e = y+1
    if y == len(map)-1:
        y_bound_e = y
    for xi in range(x_bound_s, x_bound_e+1):
        for yi in range(y_bound_s,y_bound_e+1):
            c = map[yi][xi]
            #print("checking:", x, y, "-", c,xi,yi)
            if c in symbols:
                valid = True
    return valid

main()