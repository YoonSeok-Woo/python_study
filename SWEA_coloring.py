TC = int(input())
for tc in range(1,TC+1):
    paper = [[0]*10 for i in range(10)]
    N = int(input())
    for k in range(N):
        x1,y1,x2,y2,color = map(int,input().split())
        for i in range(y1, y2 + 1):
            for j in range(x1,x2+1):
                if paper[i][j]!=0 and paper[i][j]!=color:
                    paper[i][j] = 3
                else:
                    paper[i][j] = color
    ans = 0
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                ans+=1
    print(f'#{tc} {ans}')