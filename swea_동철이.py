TC = int(input())
def dfs(fact, cost):
    global answer
    if cost <= answer:
        return
    if fact >=N:
        answer = max(answer,cost)
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        dfs(fact+1,cost*costs[fact][i])
        used[i] = False
def perc(n):
    return n*0.01
for tc in range(1,TC+1):
    N = int(input())
    costs = [list(map(perc,map(int,input().split()))) for i in range(N)]
    answer = 0
    used = [False]*N
    dfs(0,1)
    answer*=100

    print(f'#{tc} {round(answer,6):.6f}')