import re

def main():
    testfile = open("testdata/3a.txt", "r")
    inputfile = open("inputdata/3a.txt", "r")
    lines = inputfile.readlines()

    # Create the Map
    map = []
    for line in lines:
        sorted_lines = line.strip('\n')
        map_part = []
        for c in sorted_lines:
            map_part.append(c)
        map.append(map_part)
        #print(map_part)

    # Find Symbols
    serialNumberList = []
    for y in range(len(map)):
        #print(map[y])
        for x in range(len(map[y])):
            if not map[y][x].isdigit():
                if not map[y][x] == '.':
                    serialNumber = checkAroundYou(map, x, y) # Call a check around you function
                    #print(x, y, map[y][x], serialNumber)
                    for i in range(len(serialNumber)):
                        #if serialNumber[i] == '13.':
                        #    print(x, y, map[y][x], serialNumber)
                        if serialNumber[i] not in serialNumberList:
                            serialNumberList.append(serialNumber[i])
                    map[y][x] = '.'
    #print(serialNumberList)
    serialSum = 0
    for serNo in serialNumberList:
        serialSum += int(serNo)
    print(serialSum)
    testMap = []
    for mapPart in map:
        #print(mapPart)
        tempString = ''
        for p in mapPart:
            tempString += p
        testMap.append(tempString)
    for t in testMap:
        outputfile = open("testdata/3output.txt", "a")
        outputfile.write(t + '\n')
        outputfile.close
    #print(testMap)



#UL UU UR | (x-1,y-1)   (x,y-1) (x+1,y-1)
#LL CC RR | (x-1,y)     (x,y)   (x+1,y)
#DL DD DR | (x-1,y+1)   (x,y+1) (x+1,y+1)
def checkAroundYou(map, x, y):
    x_width = len(map[y])
    y_width = len(map)
    numberList = []
    # Check Upper Left (UL)
    if y > 0 and x > 0:
        if map[y-1][x-1].isdigit():
            direction = "UL"
            number = foundANumber(map, direction, x-1, y-1)
            numberList.append(number)
    # Check Upper (UU)
    if y > 0:
        if map[y-1][x].isdigit():
            direction = "UU"
            number = foundANumber(map, direction, x, y-1)
            numberList.append(number)
    # Check Upper Right (UR)
    if y > 0 and x < x_width:
        if map[y-1][x+1].isdigit():
            direction = "UR"
            number = foundANumber(map, direction, x+1, y-1)
            numberList.append(number)
    # Check Left (LL)
    if x > 0:
        if map[y][x-1].isdigit():
            direction = "LL"
            number = foundANumber(map, direction, x-1, y)
            numberList.append(number)
    # Check Right (RR)
    if x < x_width:
        if map[y][x+1].isdigit():
           direction = "RR"
           number = foundANumber(map, direction, x+1, y)
           numberList.append(number)
    # Check Down Left (DL)
    if x > 0 and y < y_width:
        if map[y+1][x-1].isdigit():
            direction = "DL"
            number = foundANumber(map, direction, x-1, y+1)
            numberList.append(number)
    # Check Down (DD)
    if y < y_width:
        if map[y+1][x].isdigit():
            direction = "DD"
            number = foundANumber(map, direction, x, y+1)
            numberList.append(number)
    # Check Down Right (DR)
    if x < x_width and y < y_width:
        if map[y+1][x+1].isdigit():
            direction = "DR"
            number = foundANumber(map, direction, x+1, y+1)
            numberList.append(number)
    return numberList

def foundANumber(map, dir, x, y):
    number = ''
    x_width = len(map[y])
    if dir == "UL":
        for i in range(x,-1,-1):
            if map[y][i].isdigit():
                number = map[y][i] + number
                map[y][i] = '.'
            elif map[y][i] == '.':
                break
        for j in range(x+1,x_width,1):
            if map[y][j].isdigit():
                number = number + map[y][j]
                map[y][j] = '.'
            elif map[y][j] == '.':
                break
    elif dir == "UU":
        for i in range(x,-1,-1):
            if map[y][i].isdigit():
                number = map[y][i] + number
                map[y][i] = '.'
            elif map[y][i] == '.':
                break
        for j in range(x+1,x_width,1):
            if map[y][j].isdigit():
                number = number + map[y][j]
                map[y][j] = '.'
            elif map[y][j] == '.':
                break
    elif dir == "UR":
        for i in range(x,-1,-1):
            if map[y][i].isdigit():
                number = map[y][i] + number
                map[y][i] = '.'
            elif map[y][i] == '.':
                break
        for j in range(x+1,x_width,1):
            if map[y][j].isdigit():
                number = number + map[y][j]
                map[y][j] = '.'
            elif map[y][j] == '.':
                break
    elif dir == "LL":
        for i in range(x,-1,-1):
            if map[y][i].isdigit():
                number = map[y][i] + number
                map[y][i] = '.'
            elif map[y][i] == '.':
                break
    elif dir == "RR":
        for j in range(x,x_width,1):
            if map[y][j].isdigit():
                number = number + map[y][j]
                map[y][j] = '.'
            elif map[y][j] == '.':
                break
    elif dir == "DL":
        for i in range(x,-1,-1):
            if map[y][i].isdigit():
                number = map[y][i] + number
                map[y][i] = '.'
            elif map[y][i] == '.':
                break
        for j in range(x+1,x_width,1):
            if map[y][j].isdigit():
                number = number + map[y][j]
                map[y][j] = '.'
            elif map[y][j] == '.':
                break
    elif dir == "DD":
        for i in range(x,-1,-1):
            if map[y][i].isdigit():
                number = map[y][i] + number
                map[y][i] = '.'
            elif map[y][i] == '.':
                break
        for j in range(x+1,x_width,1):
            if map[y][j].isdigit():
                number = number + map[y][j]
                map[y][j] = '.'
            elif map[y][j] == '.':
                break
    elif dir == "DR":
        for i in range(x,-1,-1):
            if map[y][i].isdigit():
                number = map[y][i] + number
                map[y][i] = '.'
            elif map[y][i] == '.':
                break
        for j in range(x+1,x_width,1):
            if map[y][j].isdigit():
                number = number + map[y][j]
                map[y][j] = '.'
            elif map[y][j] == '.':
                break
    return number

main()