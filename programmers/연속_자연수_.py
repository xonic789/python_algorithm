n = 15
answer = 1
m = int(n / 2) + 1
lt = 1
sum = 0

for rt in range(1, m + 1):
    sum += rt
    if sum % n == 0:
        answer += 1
    elif sum > n:
        while rt > lt:
            sum -= lt
            lt += 1
            if sum % n == 0:
                answer += 1
                break

print(answer)
