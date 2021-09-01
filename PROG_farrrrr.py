from queue import Queue
def bfs(i,con,visit):
    q = Queue()
    q.put((i,0))
    visit[i]=True
    longest = 0
    res = 0
    while not q.empty():
        now,n = q.get()
        if(longest < n):
            res=1
            longest = n
        elif longest==n:
            res+=1
        for k in con[now]:
            if visit[k]:
                continue
            visit[k]=True
            q.put((k,n+1))
    return res
def solution(n, edge):
    answer = 0
    con = [[] for i in range(n+1)]
    visit = [False]*(n+1)
    for i in edge:
        con[i[0]].append(i[1])
        con[i[1]].append(i[0])
    answer = bfs(1,con,visit)
    return answer