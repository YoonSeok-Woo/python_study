import itertools
TC = int(input())
def sum_squar(a,C):
    res = 0
    temp = 0
    for i in a:
        temp+=i
        if temp>C:
            break
        res+=i**2
        
    return res

for tc in range(1,TC+1):
    N,M,C = map(int,input().split())
    bees = []
    ans = 0
    for i in range(N):
        bees.append(list(map(int,input().split())))
    for i in range(N):
        for j in range(N-M+1):
            temp1 = bees[i][j:j+M]
            a = itertools.permutations(temp1)
            t1 =0
            for x in a:
                t1 = max(t1,sum_squar(x,C))
            for k in range(N):
                for l in range(N-M+1):
                    if k==i and j-M+1<=l<j+M:
                        continue
                    temp2 = bees[k][l:l+M]
                    b = itertools.permutations(temp2)
                    t2 = 0
                    for y in b:
                        t2 = max(t2,sum_squar(y,C))
                    #if ans<t1+t2:
                        #print(i,j,k,l,temp1,temp2,M,C,t1+t2,t1,t2)
                    ans = max(ans,(t1+t2))
                    
    print(f'#{tc} {ans}')