p = [[5,3,2,2,1]]
q = [[7,2,4]]
def dfs(p,q):
    if len(p)==len(q):
        p.sort()
        for i in range(len(p)):
            if q[i]!=p[i]:
                return False
        return True
    ans = False
    l = len(p)
    mq = max(q)
    for i in range(l):
        for j in range(i+1,l):
            temp = p[:]
            t1 = temp.pop(i)
            print(temp,p,i,j)
            t2 = temp.pop(j)
            if t2>mq:
                continue
            temp.append(t1+t2)
            ans = ans or dfs(temp,q)
    return ans
def solution(p, q):
    answer = []
    s = len(p)
    for i in range(s):
        answer.append(dfs(p[i],sorted(q[i])))
    return answer
print(solution(p,q))