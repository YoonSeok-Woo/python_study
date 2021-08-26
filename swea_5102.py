from queue import Queue
TC = int(input())

def bfs(S,G,visit,con):
    q = Queue()
    front = 0
    q.put((S,0))
    visit[S] = True
    while not q.empty():
        now, ans = q.get()
        front+=1
        for next in con[now]:
            if visit[next]:
                continue
            if next == G:
                return ans+1
            q.put((next,ans+1))
            visit[next] = True
    return 0
for tc in range(1,TC+1):
    V, E = map(int,input().split())
    con = list([] for i in range(V+1))
    for i in range(E):
        a, b = map(int,input().split())
        con[a].append(b)
        con[b].append(a)
    visit = [False]*(V+1)
    S, G = map(int,input().split())
    print(f'#{tc} {bfs(S,G,visit,con)}')