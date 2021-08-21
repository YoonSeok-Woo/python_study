def pl(i,s):
    k = 1
    res = 0
    if s[i]!=' ':
        res = 1
    while i+k < len(s) and i-k>=0:
        if s[i+k]==s[i-k] and s[i+k]!=' ':
            res+=2
            #print(s[i+k], s[i-k], res)
        elif s[i+k]!=s[i-k]:
            break
        k+=1
    return res
def solution(s):
    answer = 0
    new_s = ''
    l = len(s)
    for i in range(l):
        new_s+=s[i]
        if i<l-1:
            new_s+=' '
    for i, c in enumerate(new_s):
        temp = pl(i,new_s)
        if temp>answer:
            answer = temp
    return answer
for _ in range(10):
    tc = int(input())
    board = []
    for i in range(100):
        board.append(input())
    ans = 0
    for i in range(100):
        temp = solution(board[i])
        if temp>ans:
            ans = temp
        ts = ''
        for j in range(100):
            ts +=board[j][i]
        temp = solution(ts)
        if temp>ans:
            ans = temp
    print(f'#{tc} {ans}')
