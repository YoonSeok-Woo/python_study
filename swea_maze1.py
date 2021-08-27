from queue import Queue
TC = 10
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j,visit,maze):
    q = Queue()
    q.put((i,j))
    while not q.empty():
        x,y = q.get()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or ny<0 or nx>=16 or ny>=16:
                continue
            if visit[nx][ny] or maze[nx][ny] == 1:
                continue
            if maze[nx][ny]==3:
                return 1
            q.put((nx,ny))
            visit[nx][ny] = True
    return 0
for _ in range(1,TC+1):
    tc = int(input())
    maze = []
    for x in range(16):
        maze.append(list(map(int,input())))
        for y in range(16):
            if maze[x][y] == 2:
                si,sj = x,y
    visit = [[False]*16 for x in range(16)]
    print(f'#{tc} {bfs(si,sj,visit,maze)}')