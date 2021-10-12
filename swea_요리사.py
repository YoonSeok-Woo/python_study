from itertools import combinations
TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    taste = [list(map(int,input().split())) for i in range(N)]
    nums = [x for x in range(N)]
    cases = list(combinations(nums,N//2))
    answer = 987654321
    #print(cases)
    for case in cases:
        As = [False]*N
        for i in case:
            As[i]=True
        A = []
        B = []

        for i in range(N):
            if As[i]:
                A.append(i)
            else:
                B.append(i)
        #print(len(A), len(B))
        tA = 0
        tB = 0
        for i in range(N//2):
            for j in range(i+1,N//2):
                #print(A[i],A[j])
                #print(B[i],B[j])
                tA += taste[A[i]][A[j]]
                tA+= taste[A[j]][A[i]]
                tB += taste[B[i]][B[j]]
                tB += taste[B[j]][B[i]]
        answer = min(answer,abs(tA-tB))
    print(f'#{tc} {answer}')
    print()