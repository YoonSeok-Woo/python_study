TC = int(input())
di = [0,1,0,-1]
dj = [1,0,-1,0]

def dfs(i,j):
    global N
    if counts[board[i][j]]:
        return counts[board[i][j]]
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni < 0  or nj < 0 or ni >= N or nj >=N:
            continue
        if board[ni][nj]-board[i][j] !=1:
            continue
        else:
            counts[board[i][j]] = dfs(ni,nj)+1
            return counts[board[i][j]]

    counts[board[i][j]] = 1
    return 1

for tc in range(1,TC+1):
    N = int(input())
    board = [list(map(int,input().split())) for i in range(N)]
    counts = [0]*(N*N+1)
    for i in range(N):
        for j in range(N):
            if counts[board[i][j]]!=0:
                continue
            dfs(i,j)
    mc = max(counts)
    ans = -1
    #print(counts)
    for i in range(1,N*N+1):
        if counts[i] == mc:
            ans = i
            break
    print(f'#{tc} {ans} {mc} ')