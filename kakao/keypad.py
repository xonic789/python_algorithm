numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
answer = ''

keypad = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]
lp = [3, 0]
rp = [3, 2]

for number in numbers:
    num = str(number)
    if num == '1' or num == '4' or num == '7':
        for i in range(len(keypad)):
            if num == keypad[i][0]:
                lp[0] = i
                lp[1] = 0
                break
        answer += 'L'
    elif num == '3' or num == '6' or num == '9':
        for i in range(len(keypad)):
            if num == keypad[i][2]:
                rp[0] = i
                rp[1] = 2
                break
        answer += 'R'
    else:
        for i in range(len(keypad)):
            if num == keypad[i][1]:
                right = abs(rp[0]-i)+abs(rp[1]-1)
                left = abs(lp[0]-i)+abs(lp[1]-1)
                if right == left:
                    if hand == 'right':
                        rp[0] = i
                        rp[1] = 1
                        answer += 'R'
                    else:
                        lp[0] = i
                        lp[1] = 1
                        answer += 'L'
                    break
                if right < left:
                    rp[0] = i
                    rp[1] = 1
                    answer += 'R'
                else:
                    lp[0] = i
                    lp[1] = 1
                    answer += 'L'
                    break




print(answer)













