TC = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for tc in range(1, TC+1):
    N = int(input())
    count = 1
    ans = list(list(0 for i in range(N)) for i in range(N))
    i,j = 0, 0
    ans[i][j]=1
    dir = 0
    while count < N**2:
        flag = False
        ni, nj = i+dx[dir],j+dy[dir]
        if ni>=N or nj>=N or ni<0 or nj<0:
            flag = True
        elif ans[ni][nj]!=0:
            flag = True
        if flag :
            dir = (dir+1)%4
            ni, nj = i+dx[dir],j+dy[dir]
        count+=1
        ans[ni][nj] = count
        i, j = ni, nj
    print(f'#{tc}')
    for i in ans:
        for j in i:
            print(j, end = ' ')
        print()