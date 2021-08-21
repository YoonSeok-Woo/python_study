import queue

TC = 10
for _ in range(1,TC+1):
    tc, N = map(int,input().split())
    visit = [False]*100
    info = list(map(int,input().split()))
    j = 0
    grp = [[] for x in range(100)]
    for i in range(N):
        #print(j)
        grp[info[j]].append(info[j+1])
        j+=2
    q = queue.Queue()
    q.put(0)
    visit[0] = True
    ans = 0
    while not q.empty():
        now = q.get()
        if now == 99:
            ans = 1
            break
        for i in grp[now]:
            if visit[i]:
                continue
            q.put(i)
            visit[i]=True
    print(f'#{tc} {ans}')