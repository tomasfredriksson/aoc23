def main():
    testfile = open("testdata/4a.txt", "r")
    inputfile = open("inputdata/4a.txt", "r")
    lines = inputfile.readlines()

    cards = []
    for line in lines:
        sorted_lines = line.split(':')
        card = [sorted_lines[0]]
        numbers = sorted_lines[1].strip('\n')
        temp_numbers = numbers.split('|')
        card.append(temp_numbers[0])
        card.append(temp_numbers[1])
        #print(card)
        cards.append(card)
    
    for y in range(len(cards)):
        cards[y].append(1)

    #all_scores = 0
    bonus_cards = 0
    for c in range(len(cards)):
        #print(cards[c])
        card_no = cards[c][0].strip('Card ')
        winning_numbers = cards[c][1].strip(' ')
        having_numbers = cards[c][2].strip(' ')
        i_win = winning_numbers.split(' ')
        while('' in i_win):
            i_win.remove('')
        i_have = having_numbers.split(' ')
        while('' in i_have):
            i_have.remove('')
        score = 0
        for num in i_have:
            if num in i_win:
                score += 1
        #print(card_no, score)
        for i in range(score):
            cards[c+i+1][3] += 1*cards[c][3]
        #all_scores += score
    no_cards = 0
    for k in range(len(cards)):
        no_cards += cards[k][3]
    #print("pt1", all_scores)
    print('pt2', no_cards)

main()