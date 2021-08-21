TC = int(input())
for tc in range(1,TC+1):
    stack = []
    word = input()
    for c in word:
        if len(stack)==0:
            stack.append(c)
        else:
            if stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
    print(f"#{tc} {len(stack)}")