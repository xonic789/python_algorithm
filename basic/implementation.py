n = int(input())
move = input().split()
# λΆ λ λ¨ μ
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x = 1
y = 1
temp = 0

for i in range(len(move)):

    if move[i] == 'U':
        temp = 0
    elif move[i] == 'R':
        temp = 1
    elif move[i] == 'D':
        temp = 2
    else:
        temp = 3

    if x + dx[temp] > 0 and y + dy[temp] > 0:
        x += dx[temp]
        y += dy[temp]

print(x, y)