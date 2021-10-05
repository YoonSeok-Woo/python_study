TC = int(input())
answer = 987654321
def DFS(now, sum):
    global answer
    if not False in visited:
        answer = min(answer,sum+costs[now][0])
    for next in range(N):
        if visited[next]:
            continue
        if sum+costs[now][next]>answer:
            continue
        visited[next] = True
        DFS(next,sum+costs[now][next])
        visited[next] = False


for tc in range(1,TC+1):
    N = int(input())
    answer = 98754321
    costs = [list(map(int,input().split())) for i in range(N)]
    starting = 0
    visited = [False]* N
    visited[0] = True
    DFS(0,0)
    print(f'#{tc} {answer}')