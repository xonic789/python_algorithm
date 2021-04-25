s = input()
result = int(s[0])

for i in range(1, len(s)):
    temp = int(s[i])
    if result <= 1 or temp <= 1:
        result += temp
    else:
        result *= temp

print(result)


