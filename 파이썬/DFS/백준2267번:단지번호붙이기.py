N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

visit = [[False] * N for _ in range(N)]

result = []
each = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    global each
    each += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N :
            if graph[nx][ny] == 1 and visit[nx][ny] == False:
                visit[nx][ny] = True
                dfs(nx, ny)



for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visit[i][j] == False:
            visit[i][j] = True
            each = 0
            dfs(i, j)
            result.append(each)


result.sort()

print(len(result))
for i in result:
    print(i)

