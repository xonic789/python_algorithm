clothes =[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

answer = {}
value = 1
for clothes, kind in clothes:
    if kind in answer:
        answer[kind] += 1
    else:
        answer[kind] = 1

for i in answer:
    value *= answer[i] + 1

print(value-1)