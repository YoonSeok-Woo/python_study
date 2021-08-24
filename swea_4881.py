TC = int(input())
ans = 100000
def dfs(i,N,sm):
    if i == N :
        return sm
    global ans
    for j in range(N):
        if used[j]:
            continue
        if ans <sm:
            continue
        used[j]=True
        tsm=sm+arr[i][j]
        ans = min(ans,dfs(i+1,N,tsm))
        used[j]=False
    return ans
for tc in range(1,TC+1):
    N = int(input())
    arr = []
    used = [False]*N
    for i in range(N):
        arr.append(list(map(int,input().split())))
    ans = 1000000
    for i in range(N):
        ans = min(ans,dfs(0,N,0))
    print(f'#{tc} {ans}')
