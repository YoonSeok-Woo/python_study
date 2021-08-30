TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    farm = []
    for i in range(N):
        farm.append(list(map(int,input())))
    center = N//2
    ans = 0
    for i in range(N):
        for j in range(center-(center-abs(center-i)),center+(center-abs(center-i))+1):
            ans+=farm[i][j]
            #print(i,j)
    print(f'#{tc} {ans}')