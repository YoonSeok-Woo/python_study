TC = 10
def mt(pattern):
    l = len(pattern)
    table = [0]*l
    j = 0
    for i in range(1,l):
        while j>0 and pattern[i]!=pattern[j]:
            j = table[j-1]
        if pattern[i]==pattern[j]:
            j+=1
            table[i] = j
    return table

for _ in range(TC):
    tc = int(input())
    pattern = input()
    target = input()
    table = mt(pattern)
    j = 0
    count = 0
    lp = len(pattern)
    for t in target:
        while j>0 and t!=pattern[j]:
            j = table[j-1]
        if t==pattern[j]:
            if j == lp-1:
                count+=1
                j= table[j]
            else:
                j+=1
    print(f'#{tc} {count}')