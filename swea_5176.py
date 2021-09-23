TC = int(input())
def mktree(n):
    if n>N:
        return
    global order
    mktree(2*n)
    tree[n] = order
    order+=1
    mktree(2*n+1)
for tc in range(1,TC+1):
    N = int(input())
    tree = [0]*(N+1)
    order = 1
    mktree(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
