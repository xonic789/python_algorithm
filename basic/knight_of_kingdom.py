location = input()

column = int(ord(location[0])) - int(ord('a')) + 1
row = int(location[1])
answer = 0

# 북좌우 동위아래 남좌우 서위아래
moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]


for move in moves:
    # 이동하고자 하는 위치 확인
    next_row = row + move[0]
    next_column = column + move[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        answer += 1
print(answer)
