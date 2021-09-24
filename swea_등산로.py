TC = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(x,y,used,count):
    res = count
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]

        if nx<0 or ny <0 or nx>=N or ny >=N or visit[nx][ny]:
            continue
        temp = mountain[nx][ny]
        if mountain[nx][ny] >= mountain[x][y] and used:
            continue
        if mountain[nx][ny] >= mountain[x][y] and not used:
            if mountain[nx][ny]-K <mountain[x][y]:
                mountain[nx][ny] = mountain[x][y]-1
                visit[nx][ny]=True
                res = max(res, dfs(nx,ny,True,count+1))
                mountain[nx][ny] = temp
                visit[nx][ny]=False
            else:
                continue
        else:
            visit[nx][ny]=True
            res = max(res,dfs(nx,ny,used,count+1))
            visit[nx][ny]=False
    return res
for tc in range(1,TC+1):
    N, K = map(int,input().split())
    top = 0
    mountain = []
    visit = [[False]*N for i in range(N)]
    for i in range(N):
        nums = list(map(int,input().split()))
        mountain.append(nums)
        for j in range(N):
            top = max(nums[j],top)
    sps = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j]== top:
                sps.append([i,j])
    ans = 0
    for sp in sps:
        visit[sp[0]][sp[1]]=True
        ans = max(ans, dfs(sp[0],sp[1],False,1))
        visit[sp[0]][sp[1]]=False

    print(f'#{tc} {ans}')