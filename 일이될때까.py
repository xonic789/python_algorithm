n, k = map(int, input().split())
count = 0

while True:
    if n % k == 0:
        count += 1
        n /= k
    else:
        n -= 1
        count += 1
    if n == 0:
        break

print(count)
