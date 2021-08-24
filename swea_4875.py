TC = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs(x, y, N):
    #print(x,y)
    if maze[x][y]==3:
        return True
    maze[x][y]=1
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if nx<0 or ny<0 or nx>=N or ny >=N:
            continue
        if maze[nx][ny]==1:
            continue
        if maze[nx][ny]==3:
            return True
        if dfs(nx,ny,N):
            return True
    return False

for tc in range(1,TC+1):
    maze = []
    N = int(input())
    for i in range(N):
        maze.append(list(map(int,list(input()))))
        for j in range(N):
            #print(maze[i])
            if maze[i][j]==2:
                si, sj = i, j
    #print(si,sj,maze[si][sj])
    if dfs(si,sj,N):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')