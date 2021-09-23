TC = int(input())
def treesum(n):
    if tree[n]!=0:
        return tree[n]
    else:
        if 2*n+1 > N:
            return treesum(2*n)
        else:
            return treesum(2*n)+treesum(2*n+1)
for tc in range(1,TC+1):
    N,M,L = map(int,input().split())
    tree = [0]*(N+1)
    for i in range(M):
        j, num = map(int,input().split())
        tree[j] = num
    print(f'#{tc} {treesum(L)}')
