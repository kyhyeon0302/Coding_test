// https://www.acmicpc.net/problem/2667

from collections import deque

N = int(input())
graph = []
visit = [[False] * N for i in range(N)]

answer = []
result = 0

for i in range(N):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    count = 1
    q = deque()
    q.append((x, y))
    visit[x][y] = True


    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visit[nx][ny] == False:
                    q.append((nx, ny))
                    visit[nx][ny] = True
                    count += 1

    answer.append(count)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visit[i][j] == False:
            bfs(i, j)
            result += 1

answer.sort()

print(result)
for i in answer:
    print(i)
