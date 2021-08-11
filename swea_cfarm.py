TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    carrots = list(map(int,input().split()))
    sc = []
    num = 0
    for i in carrots:
        num+=i
        sc.append(num)
    ans = sc[N-1]
    aind = -1
    for i,num in enumerate(sc):
        left = num
        right = sc[N-1]-left
        if abs(right-left)<ans:
            ans = abs(right-left)
            aind = i+1

    print(f'#{tc} {aind} {ans}')


