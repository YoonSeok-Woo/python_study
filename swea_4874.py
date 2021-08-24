TC = int(input())
for tc in range(1,TC+1):
    stack = []
    command = list(input().split())
    for i in command:
        if len(i)>=2 or '0'<=i<='9':
            stack.append(int(i))
        else:
            if i=='.':
                if len(stack)>=2:
                    print(f'#{tc} error')
                else:
                    print(f'#{tc} {stack.pop()}')
            elif len(stack)<2:
                print(f'#{tc} error')
                break
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                if i == '*':
                    stack.append(t1*t2)
                elif i == '+':
                    stack.append(t1+t2)
                elif i == '-':
                    stack.append(t2-t1)
                elif i== '/':
                    stack.append(t2//t1)