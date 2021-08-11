TC = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for tc in range(1,TC+1):
    N = int(input())
    board = []
    ans = 0
    for i in range(N):
        board.append(list(map(int,input().split())))
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i+dx[k]
                nj = j+dy[k]
                if ni<0 or ni>=N or nj<0 or nj>=N:
                    continue
                ans+=abs(board[i][j]-board[ni][nj])
    print(f'#{tc} {ans}')