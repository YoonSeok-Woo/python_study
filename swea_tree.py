TC = 10
def inorder(i):
    l = len(tree[i])
    if l >=2:
        inorder(tree[i][1])
    print(tree[i][0],end = '')
    if l==3:
        inorder(tree[i][2])
for tc in range(1,TC+1):
    N = int(input())
    tree = [[] for i in range(N+1)]
    for i in range(N):
        inp = list(input().split())
        tree[int(inp[0])].append(inp[1])
        for j in range(2,len(inp)):
            tree[int(inp[0])].append(int(inp[j]))
    #print(tree)
    print(f'#{tc}',end = ' ')
    inorder(1)
    print()