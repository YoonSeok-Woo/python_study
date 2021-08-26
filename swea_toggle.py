TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    board = list(list(map(int,input().split())) for i in range(N))
    for k in range(1,M+1):
        for i in range(N):
            for j in range(N):
                ri = i+1
                rj = j+1
                if M%k ==0:
                    board[i][j] = 1-board[i][j]
                elif (ri+rj)%k==0:
                    board[i][j]=1-board[i][j]
    ans = 0
    for i in range(N):
        for j in range(N):
            ans+=board[i][j]
    print(f'#{tc} {ans}')