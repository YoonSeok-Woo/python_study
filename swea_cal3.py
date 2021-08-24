TC = 10
isp = {')': -1,'*':2,'/':2,'+':1,'-':1,'(':0}
icp = {')':-1,'*':2,'/':2,'+':1,'-':1,'(':3}
for tc in range(1,TC+1):
    _ = int(input())
    exp = input()
    stack_num = []
    stack_op = []
    for c in exp:
        #print(c, stack_op,stack_num)
        if '0'<=c<='9':
            stack_num.append(c)
        elif c==')':
            while stack_op and stack_op[-1]!='(':
                stack_num.append(stack_op.pop())
            stack_op.pop()
        elif len(stack_op)==0:
            stack_op.append(c)
        elif isp[stack_op[-1]]>=icp[c]:
            while isp[stack_op[-1]]>=icp[c]:
                stack_num.append(stack_op.pop())
            stack_op.append(c)
        else:
            stack_op.append(c)
    while stack_op:
        stack_num.append(stack_op.pop())
    #print(stack_num)
    stack = []
    for c in stack_num:
        if '0'<=c<='9':
            stack.append(int(c))
        else:
            t2 = stack.pop()
            t1 = stack.pop()
            if c == '*':
                stack.append(t1*t2)
            elif c=='/':
                stack.append(t1//t2)
            elif c=='+':
                stack.append(t1+t2)
            elif c=='-':
                stack.append(t1-t2)
    print(f'#{tc} {stack[0]}')
