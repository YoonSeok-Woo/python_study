TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    board = [list(input()) for i in range(N)]
    ans = False
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for k in range(5):
                    if j+k>=N or board[i][j+k] != 'o':
                        break
                else:
                    ans = True
                for k in range(5):
                    if i+k>=N or board[i+k][j] != 'o':
                        break
                else:
                    ans = True
                for k in range(5):
                    if i+k >=N or j+k >= N or board[i+k][j+k]!='o':
                        break
                else:
                    ans = True
                for k in range(5):
                    if i+k>=N or j-k <0 or board[i+k][j-k]!='o':
                        break
                else:
                    ans = True
                if ans:
                    break
        if ans:
            break
    if ans:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
