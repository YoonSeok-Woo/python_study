T = int(input())
for tc in range(1,T+1):
    N = int(input())
    list_A = []
    list_B = []
    for i in range(N):
        tA,tB = map(int,input().split())
        list_A.append(tA)
        list_B.append(tB)
    P = int(input())
    print(f'#{tc}', end = ' ')
    for i in range(P):
        tC = int(input())
        count = 0
        for j in range(N):
            if list_A[j]<=tC<=list_B[j]:
                count+=1
        print(count, end = ' ')
    print()