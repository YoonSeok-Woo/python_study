TC = int(input())
def dfs(ind, height):
    global answer
    if height >=target:
        answer = min(height-target, answer)
        return
    if ind >=N:
        return
    dfs(ind+1, height+tall[ind])
    dfs(ind+1, height)
for tc in range(1,TC+1):
    N, target = map(int,input().split())
    tall = list(map(int,input().split()))
    answer = 987654321
    dfs(0,0)
    print(f'#{tc} {answer}')