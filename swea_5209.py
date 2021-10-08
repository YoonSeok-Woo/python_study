TC = int(input())
def dfs(fact, cost):
    global answer
    if cost >= answer:
        return
    if fact >=N:
        answer = min(answer,cost)
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        dfs(fact+1,cost+costs[fact][i])
        used[i] = False

for tc in range(1,TC+1):
    N = int(input())
    costs = [list(map(int,input().split())) for i in range(N)]
    answer = 987654321
    used = [False]*N
    dfs(0,0)
    print(f'#{tc} {answer}')