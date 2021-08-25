TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    wall = list(list(map(int,input().split())) for x in range(N))
    wp = list([False]*M for x in range(M))
    for i in range(M):
        wp[i][i] = True
        wp[i][M-i-1] = True
        #print(wp[i])
    ans = 0
    #case = 0
    for k in range(0 , N-M+1):
        for l in range(0 ,N-M+1):
            temp = 0
            for i in range(M):
                for j in range(M):
                    #print(i + k, j + l, case)
                    if i+k<0 or j+l<0 or i+k>=N or j+l>=N:
                        continue
                    if not wp[i][j]:
                        continue
                    temp+=wall[i+k][j+l]

            #case +=1
            if temp > ans:
                ans = temp
    print(f'#{tc} {ans}')