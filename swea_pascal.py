TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    ans = list([0]*N for x in range(N))
    ans[0][0]=1
    for i in range(1,N):
        for j in range(i+1):
            if j==0:
                ans[i][j]=ans[i-1][j]
            else:
                ans[i][j] =ans[i-1][j]+ans[i-1][j-1]
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(ans[i][j], end=' ')
        print()