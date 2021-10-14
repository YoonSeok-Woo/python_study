from collections import deque
TC = int(input())

def bfs(N,M):
    q = deque()
    visit = [False]*1000001
    q.append((N,0))
    visit[N]=True
    while q:
        now,count = q.popleft()
        nexts = [now+1,now-1,now-10,now*2]
        for next in nexts:
            if next <1 or next>1000000:
                continue
            if visit[next]:
                continue
            if next==M:
                return count+1
            q.append((next,count+1))
            visit[next] = True

for tc in range(1,TC+1):
    N, M = map(int,input().split())

    print(f'#{tc} {bfs(N,M)}')