from collections import deque
n = 5
m = 6
# 괴물이 있는 곳은 0
# 괴물이 없는 곳은 1
# 시작 지점은 0,0 끝 지점은 n-1,m-1

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

# 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 처음 방문
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]



print(bfs(0, 0))






