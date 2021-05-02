clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

answer = 1

dic = {}
temp = ''
for clothes, kind in clothes:
    # hash에 옷의 종류가 존재하면 기존 값에다 1을 더 해준다.
    # 경우의 수 합법칙
    if kind in dic:
        dic[kind] += 1
        temp = kind
    # 없으면 1로 초기화한다.
    else:
        dic[kind] = 1

# 경우의 수 곱법칙

if len(dic) == 1:
    answer = dic[temp]
else:
    for kind in dic:
        answer *= dic[kind] + 1

print (answer - 1)