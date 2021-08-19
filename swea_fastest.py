TC = int(input())
for tc in range(1,TC+1):
    A, B = input().split()
    i = 0
    lA = len(A)
    lB = len(B)
    ans=0
    while i<lA:
        ans+=1
        if A[i:i+lB]==B:
            i+=lB-1
        i+=1

    print(f'#{tc} {ans}')