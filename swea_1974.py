TC = int(input())
for tc in range(1,TC+1):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int,input().split())))
    #print(sudoku)
    ans = True
    for i in range(9):
        checking = set()
        for j in range(9):
            checking.add(sudoku[i][j])
        if len(checking)!=9:
            ans = False
            break
    for j in range(9):
        checking = set()
        for i in range(9):
            checking.add(sudoku[i][j])
        if len(checking)!=9:
            ans= False
            break
    for i in range(3):
        for j in range(3):
            checking = set()
            for k in range(3):
                for l in range(3):
                    checking.add(sudoku[i*3+k][j*3+l])
            if len(checking)!=9:
                ans = False
                break
        if ans==False:
            break
    if ans:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')