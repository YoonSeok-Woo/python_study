TC = 10
for tc in range(1,TC+1):
    nono = input()
    ladder = []
    for i in range(100):
        ladder.append(list(map(int,input().split())))
    end = -1
    for i,num in enumerate(ladder[99]):
        if num ==2:
            end = i
    i = 99
    j = end
    dy = -1
    dx = 0
    while i!=0:
        if dx==0:
            if j-1>=0:
                if ladder[i][j-1]==1:
                    dy = 0
                    dx = -1
            if j+1<100:
                if ladder[i][j+1]==1:
                    dy = 0
                    dx = 1
        else :
            if ladder[i-1][j]==1:
                dy = -1
                dx = 0
        i = i+dy
        j = j+dx
        if i==0:
            ans = j
            break
    print(f'#{tc} {ans}')