TC = int(input())

def counting(N):
    global count
    count+=1
    for i in range(2):
        if len(tree[N])<=i:
            break
        counting(tree[N][i])
for tc in range(1,TC+1):
    E, N = map(int,input().split())
    inputs = list(map(int,input().split()))
    tree = [[] for x in range(E+2)]
    for i in range(E):
        tree[inputs[2*i]].append(inputs[2*i+1])
    count = 0
    counting(N)
    print(f'#{tc} {count}')
    #print(tree)