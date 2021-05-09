def solution(code, day, data):
    answer = []
    price = 0
    time = ''
    tcode = ''
    for i in range(len(data)):
        temp = data[i].split(" ")
        for t in temp:
            a = t.split("=")
            if a[0] == 'price':
                price = int(a[1])
            elif a[0] == 'code':
                tcode = a[1]
            elif a[0] == 'time':
                time = a[1]
        if tcode == code:
            if time[:len(day)] == day:
                answer.append([price, time])
        price = 0
        tcode = ''
        time = ''

    temp = sorted(answer, key=lambda x:x[1])
    answer = []
    for i in temp:
        answer.append(i[0])


    return answer
print(solution("012345", "20190620", ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]))
