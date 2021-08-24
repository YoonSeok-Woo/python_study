TC = 10
for tc in range(1, TC+1):
    N = int(input())
    com = input()
    stack = []
    stack_temp = []
    for i in com:
        if '0'<=i<='9':
            stack.append(int(i))
        else:
            if i == '*':
                stack_temp.append(i)
            elif i=='+':
                while stack_temp:
                    stack.append(stack_temp.pop())
                stack_temp.append(i)
    while stack_temp:
        stack.append(stack_temp.pop())
    #print(stack)
    ans = []
    for i in stack:
        if i=='*':
            t1 = ans.pop()
            t2 = ans.pop()
            ans.append(t1*t2)
        elif i=='+':
            t1 = ans.pop()
            t2 = ans.pop()
            ans.append(t1+t2)
        else:
            ans.append(i)
    print(f'#{tc} {ans[0]}')

