TC = int(input())
dx=[0,1,0,-1,1,1,-1,-1]
dy=[1,0,-1,0,1,-1,1,-1]
def rcsum(i,j,wall,N,M):
    ans1 = wall[i][j]
    for k in range(1,M):
        for l in range(4):
            ni = i+dx[l]*k
            nj = j+dy[l]*k
            if ni<0 or nj < 0 or ni>=N or nj>=N:
                continue
            ans1+=wall[ni][nj]
    ans2 = wall[i][j]
    for k in range(1,M):
        for l in range(4,8):
            ni = i+dx[l]*k
            nj = j+dy[l]*k
            if ni<0 or nj < 0 or ni>=N or nj>=N:
                continue
            ans2+=wall[ni][nj]
    #print(i,j, ans1,ans2)
    return max(ans1,ans2)

for tc in range(1,TC+1):
    N, M = map(int,input().split())
    wall = list(list(map(int,input().split())) for i in range(N))
    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans,rcsum(i,j,wall,N,M))
    print(f'#{tc} {ans}')