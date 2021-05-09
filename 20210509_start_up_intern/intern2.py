def solution(t, r):
    answer = []


    # 아이디가 0인 사람이 0번 리프트를 탐
    # 아이디가 1인 사람이 1번 리프트를 탐
    # 인덱스랑 같으면 넣어주고 같지 않으면
    for i in range(len(t)):
        if t[i] == i:
            answer.append(i)
        else:










    return answer

print(solution([0,1,3,0], [0,1,2,3]))