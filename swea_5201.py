TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    containers = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    containers.sort(reverse = True)
    trucks.sort(reverse=True)
    con = 0
    tr = 0
    ans = 0
    while con < N and tr < M:
        if containers[con] <= trucks[tr]:
            ans+= containers[con]
            con+=1
            tr+=1
        else:
            con+=1
    print(f'{tc} {ans}')