TC = 10
for tc in range(1,TC+1):
    N = int(input())
    table = []
    for i in range(N):
        table.append(list(map(int,input().split())))
    check = [[False]*N for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if check[i][j] or table[i][j]!=1:
                continue
            check[i][j] = True
            for k in range(i+1,N):
                if table[k][j] == 2:
                    check[k][j] = True
                    ans+=1
                    break
                elif table[k][j] == 1:
                    check[k][j] = True
    print(f'#{tc} {ans}')