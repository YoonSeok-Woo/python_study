import sys
TC = int(input())
sys.setrecursionlimit(15000)
def chk(film,K):
    s = len(film)
    l = len(film[0])
    for j in range(l):
        count = 1
        for i in range(1,s):
            if film[i][j]==film[i-1][j]:
                count+=1
            else:
                count = 1
            if count>=K:
                break
        if count <K:
            #print(j)
            return False    
    return True
def dfs(film, i,n,K):
    if chk(film,K):
        return n
    if i >= len(film):
        return len(film)+1
    temp = []
    for _ in film:
        temp.append(_[:])
    t = dfs(temp,i+1,n,K)
    l = len(temp[0])
    for k in range(l):
        temp[i][k] = 1
    
    t = min(t,dfs(temp,i+1,n+1,K))
    for k in range(l):
        temp[i][k] = 0
    t = min(t,dfs(temp,i+1,n+1,K))
    return t
for tc in range(1,TC+1):
    D, W, K = map(int,input().split())
    film = []
    for i in range(D):
        film.append(list(map(int,input().split())))
    print(f'#{tc} {dfs(film,0,0,K)}')
    
    

    