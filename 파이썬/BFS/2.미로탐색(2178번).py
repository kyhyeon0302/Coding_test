from collections import deque

N, M = map(int, input().split())
visit = [[False] * M for i in range(N)]

graph = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    graph.append(list(map(int, input())))


def bfs(x, y):
    q = deque()
    q.append((x, y))


    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))




bfs(0, 0)

print(graph[N-1][M-1])
