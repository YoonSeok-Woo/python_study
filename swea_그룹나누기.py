TC = int(input())
def findpar(i):
    if parent[i]==i:
        return parent[i]
    parent[i] = findpar(parent[i])
    return parent[i]
for tc in range(1, TC+1):
    N, M = map(int,input().split())
    connections = list(map(int,input().split()))
    parent = [i for i in range(N+1)]
    k = 0
    for i in range(M):
        a = findpar(connections[k])
        b = findpar(connections[k+1])
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
        k+=2
    for i in range(N+1):
        findpar(i)
    ans = len(set(parent))-1
    #print(parent)
    print(f'#{tc} {ans}')

