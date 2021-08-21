TC = int(input())
for tc in range(1,TC+1):
    target = input()
    stack = []
    ans = 1
    for c in target:
        if len(stack)==0:
            if c=='(' or c=='{':
                stack.append(c)
            if c ==')' or c=='}':
                ans = 0
                break
        else:
            if c==')':
                if stack[-1]=='{':
                    ans = 0
                    break
                else:
                    stack.pop()
            elif c=='}':
                if stack[-1]=='(':
                    ans = 0
                    break
                else:
                    stack.pop()
            elif c=='(' or c=='{':
                stack.append(c)
        #print(c, stack)
    else:
        if len(stack)!=0:
            ans = 0
    print(f'#{tc} {ans}')