TC = int(input())

def dfs(now,dis):
    global answer

    flag = True
    for next in con[now]:
        if visit[next]:
            continue
        else:
            flag = False
            visit[next] = True
            dfs(next,dis+1)
            visit[next]=False
    if flag:
        answer = max(answer,dis)
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    con = [[] for _ in range(N+1)]
    answer = 1
    visit = [False] * (N+1)
    for i in range(M):
        x,y = map(int,input().split())
        con[x].append(y)
        con[y].append(x)
    for i in range(N):
        visit[i]=True
        dfs(i,1)
        visit[i] = False
    print(f'#{tc} {answer}')