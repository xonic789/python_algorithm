def solution(s):
    answer = ''
    temp = 0
    tempstr = ''

    for i in range(len(s)):
        if s[i] <= '9':
            answer += s[i]
        else:
            tempstr += s[i]
            if tempstr == 'one':
                answer += '1'
                tempstr = ''
            elif tempstr == 'two':
                answer += '2'
                tempstr = ''
            elif tempstr == 'three':
                answer += '3'
                tempstr = ''
            elif tempstr == 'four':
                answer += '4'
                tempstr = ''
            elif tempstr == 'five':
                answer += '5'
                tempstr = ''
            elif tempstr == 'six':
                answer += '6'
                tempstr = ''
            elif tempstr == 'seven':
                answer += '7'
                tempstr = ''
            elif tempstr == 'eight':
                answer += '8'
                tempstr = ''
            elif tempstr == 'nine':
                answer += '9'
                tempstr = ''

    return int(answer)

solution("one4seveneight")