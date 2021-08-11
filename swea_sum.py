TC = 10
for tc in range(1,TC+1):
    ans = 0
    ntc = int(input())
    board = []
    for i in range(100):
        board.append(list(map(int,input().split())))
        ans = max(ans,sum(board[i]))
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += board[j][i]
        ans = max(ans,temp)
    cr1 = 0
    cr2 = 0
    for i in range(100):
        cr1+=board[i][i]
        cr2+=board[99-i][i]
    ans = max(ans,cr1,cr2)
    print(f'#{tc} {ans}')