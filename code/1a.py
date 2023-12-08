testfile = open("testdata/1a.txt", "r")
testfile2 = open("testdata/1b.txt", "r")
inputfile = open("inputdata/1a.txt", "r")

lines = inputfile.readlines()

spelled_out = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
all_codes = []
for line in lines:
    line_numbers = []
    for c in range(len(line)):
        if line[c].isdigit():
            line_numbers.append(line[c])
        else:
            if line[c] == 'o':
                if c+2 < len(line):
                    if line[c]+line[c+1]+line[c+2] == 'one':
                        line_numbers.append('1')
            elif line[c] == 't':
                if c+2 < len(line):
                    if line[c]+line[c+1]+line[c+2] == 'two':
                        line_numbers.append('2')
                if c+4 < len(line):
                    if line[c]+line[c+1]+line[c+2]+line[c+3]+line[c+4] == 'three':
                        line_numbers.append('3')
            elif line[c] == 'f':
                if c+3 < len(line):
                    if line[c]+line[c+1]+line[c+2]+line[c+3] == 'four':
                        line_numbers.append('4')
                    elif line[c]+line[c+1]+line[c+2]+line[c+3] == 'five':
                        line_numbers.append('5')
            elif line[c] == 's':
                if c+2 < len(line):
                    if line[c]+line[c+1]+line[c+2] == 'six':
                        line_numbers.append('6')
                if c+4 < len(line):
                    if line[c]+line[c+1]+line[c+2]+line[c+3]+line[c+4] == 'seven':
                        line_numbers.append('7')
            elif line[c] == 'e':
                if c+4 < len(line):
                    if line[c]+line[c+1]+line[c+2]+line[c+3]+line[c+4] == 'eight':
                        line_numbers.append('8')
            elif line[c] == 'n':
                if c+3 < len(line):
                    if line[c]+line[c+1]+line[c+2]+line[c+3] == 'nine':
                        line_numbers.append('9')

    print(line_numbers, line.strip())
    code = line_numbers[0]+line_numbers[len(line_numbers)-1]
    all_codes.append(code)
print(all_codes)
sum = 0
for codes in all_codes:
    sum += int(codes)
print(sum)