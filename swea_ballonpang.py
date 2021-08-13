TC = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    bs = []
    for i in range(N):
        bs.append(list(map(int,input().split())))
    ans = 0
    for i in range(N):
        for j in range(M):
            num = bs[i][j]
            temp = num
            for k in range(4):
                for l in range(1,num+1):
                    ni = i+l*dx[k]
                    nj = j+l*dy[k]
                    if ni >=N or nj >=M or ni<0 or nj<0:
                        break
                    else :
                        temp+=bs[ni][nj]
            if temp>ans:
                ans = temp
    print(f'#{tc} {ans}')
