'''
https://www.acmicpc.net/problem/2178
'''


from collections import deque

N, M = map(int, input().split())
visit = [[False] * M for i in range(N)]

graph = []
dx = [0, 0, -1, 1] #상하좌우 구현하기
dy = [-1, 1, 0, 0]

for i in range(N): #배열 초기화
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
                if graph[nx][ny] == 1 and visit[nx][ny] == False: #방문 x, 1있으면 수행
                    graph[nx][ny] = graph[x][y] + 1 #한 칸 이동하기 
                    q.append((nx, ny)) #q에 삽입
                    
bfs(0, 0) # bfs 수행 
print(graph[N-1][M-1]) #최소값 출력
