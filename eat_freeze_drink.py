n = 4
m = 5
# 4행 5열의 2차원 배열, 음료를 넣을 수 있는 칸은 0, 넣지 못하는 칸은 1
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False

    if graph[x][y] == 0:
        # 방문처리하기.
        graph[x][y] = 1
        # 상하좌우 돌면서 방문처리 모두 하기
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False



answer = 0

# 2차원 배열을 0,0부터 돌며 0이라면 상하좌우, 상하좌우를 재귀적으로 호출하여
# 모든 0을 1로 바꾸고 시작점이 0이었기 때문에
# 음료를 하나 만들 수 있고, 연결된 노드들을 모두 1로 만들었기 때문에
# 다시 검사하여도 0이 아니다.
# dfs를 재귀적으로 호출하여 모두 방문 처리를 한다.
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if dfs(i, j) == True:
            answer += 1

print(answer)