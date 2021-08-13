TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    wall = []
    for i in range(N):
        wall.append(list(map(int,input().split())))
    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp+=wall[i+k][j+l]
            if temp > ans:
                ans = temp
    print(f'#{tc} {ans}')