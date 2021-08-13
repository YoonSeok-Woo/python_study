TC = 10
for _ in range(10):
    tc = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int,input().split())))
    for i in range(100):
        if ladder[99][i]==2:
            X = i
    i = 99
    j = X
    dx = 0
    dy = -1
    while i > 0:
        if j-1>=0 and dx==0 and ladder[i][j-1]==1:
            dx = -1
            dy = 0
        elif j+1<100 and dx==0 and ladder[i][j+1]==1:
            dx = 1
            dy = 0
        elif dx!=0 and ladder[i-1][j]==1:
            dx = 0
            dy = -1

        i, j = i+dy, j+dx
    print(f'#{tc} {j}')