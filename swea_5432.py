TC = int(input())
for tc in range(1,TC+1):
    case = input()
    stack = []
    l = len(case)
    ans = 0
    for i in range(l):
        if case[i]=='(':
            stack.append(case[i])
        else:
            if case[i-1]=='(':
                stack.pop()
                ans+=len(stack)
            else:
                stack.pop()
                ans+=1
        #print(stack, ans)
    print(f'#{tc} {ans}')