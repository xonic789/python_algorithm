n = input()
result = []
total_int = 0

for x in n:
    # 알파벳인지 확인
    if x.isalpha():
        result.append(x)
    else:
        total_int += int(x)

result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if total_int != 0:
    result.append(str(total_int))

print(''.join(result))