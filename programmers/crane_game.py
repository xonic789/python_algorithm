board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
answer = 0
res = []

for move in moves:
    for i in range(len(board)):
        doll = board[i][move - 1]
        board[i][move - 1] = 0
        if doll != 0:
            if res and res[-1] == doll:
                res.pop()
                answer += 2
            else:
                res.append(doll)
            break
print(answer)