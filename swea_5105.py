from queue import Queue
TC = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(i, j, maze, visit,N):
    q = Queue()
    q.put((i,j,0))
    visit[i][j]=True
    while not q.empty():
        x,y,c = q.get()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if visit[nx][ny] or maze[nx][ny]==1:
                continue
            if maze[nx][ny] == 3:
                return c
            visit[nx][ny] = True
            q.put((nx,ny,c+1))
    return 0
for tc in range(1,TC+1):
    N = int(input())
    maze = []
    for i in range(N):
        maze.append(list(map(int,input())))
        for j in range(N):
            if maze[i][j]==2:
                si = i
                sj = j
    visit = list([False]*N for i in range(N))
    print(f'#{tc} {bfs(si,sj,maze,visit,N)}')