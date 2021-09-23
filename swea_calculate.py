TC = 10
def calc(n):
    if tree[n][0]=='+':
        return calc(tree[n][1])+calc(tree[n][2])
    elif tree[n][0]=='-':
        return calc(tree[n][1])-calc(tree[n][2])
    elif tree[n][0]=='*':
        return calc(tree[n][1])*calc(tree[n][2])
    elif tree[n][0]=='/':
        return calc(tree[n][1])//calc(tree[n][2])
    else:
        return tree[n][0]
for tc in range(1,TC+1):
    N = int(input())
    tree = [[] for i in range(N+1)]
    for i in range(N):
        inputs = list(input().split())
        if inputs[1] == '+' or inputs[1]=='-' or inputs[1] == '*' or inputs[1] == '/':
            tree[int(inputs[0])].append(inputs[1])
            tree[int(inputs[0])].append(int(inputs[2]))
            tree[int(inputs[0])].append(int(inputs[3]))
        else:
            tree[int(inputs[0])].append(int(inputs[1]))
    print(f'#{tc} {calc(1)}')

