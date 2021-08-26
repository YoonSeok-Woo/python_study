TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    arr = list(input().split())
    mid = N//2
    p = mid
    if N%2==1:
        p +=1
    print(f'#{tc}',end = ' ')
    for i in range(mid) :
        print(arr[i], arr[p+i], end = ' ')
    if p!=mid:
        print(arr[mid])
    else:
        print()