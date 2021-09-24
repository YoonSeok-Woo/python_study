from collections import deque
TC = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    field = []
    for i in range(N):
        field.append(input())
    ans = 0
    ground = [[-1]*M for i in range(N)]
    sps = []
    for i in range(N):
        for j in range(M):
            if field[i][j] == 'W':
                sps.append([i,j])
                ground[i][j] = 0
    q = deque()
    for sp in sps:
        q.append((sp[0],sp[1]))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx <0 or ny <0 or nx>=N or ny >=M:
                continue
            if ground[nx][ny] !=-1:
                continue
            ground[nx][ny] = ground[x][y]+1
            ans += ground[nx][ny]
            q.append((nx,ny))
    #for i in range(N):
    #    print(ground[i])
    print(f'#{tc} {ans}')