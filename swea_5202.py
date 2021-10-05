TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    containers = [list(map(int,input().split())) for i in range(N)]
    containers.sort(key = lambda x : x[1])
    count = 1
    time = containers[0][1]
    for i in range(N):
        if containers[i][0] >=time:
            count+=1
            time = containers[i][1]
    print(f'#{tc} {count}')
