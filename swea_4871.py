TC = int(input())
def bfs(now, end, count, visit,grp):
    if now==end:
        return True
    for i in grp[now]:
        if not visit[i]:
            visit[i]=True
            if bfs(i,end,count+1,visit,grp):
                return True
            #print(visit)
            visit[i]=False
    return False
for tc in range(1,TC+1):
    V, E = map(int,input().split())
    grp = list([] for i in range(V+1))
    visit = [False]*(V+1)
    for i in range(E):
        start, end = map(int,input().split())
        grp[start].append(end)
        #print(grp[start])
    start, end = map(int,input().split())
    visit[start]=True
    if bfs(start,end,1,visit,grp):
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')