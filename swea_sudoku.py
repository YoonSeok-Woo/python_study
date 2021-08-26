TC = int(input())
for tc in range(1,TC+1):
    ans = True
    board = list(list(map(int,input().split())) for x in range(9))
    if ans:

        for i in range(9):
            cl = [False] * 10
            for j in range(9):
                if cl[board[i][j]]:
                    ans = False
                    break
                cl[board[i][j]] = True
            if not ans:
                break
    if ans :

        for i in range(9):
            cl = [False] * 10
            for j in range(9):
                #print(board[j][i], end = ' ')
                if cl[board[j][i]]:
                    ans = False
                    break
                cl[board[j][i]] = True
            #print()
            if not ans:
                break

    if ans :

        for i in range(9):
            cl = [False] * 10
            for j in range(9):
                ni = i//3*3+j//3
                nj = i%3*3+j%3
                if cl[board[ni][nj]]:
                    ans = False
                    break
                cl[board[ni][nj]] = True
            if not ans:
                break
    if ans:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')