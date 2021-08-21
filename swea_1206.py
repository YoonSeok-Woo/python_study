TC = 10
for tc in range(1,TC+1):
    N = int(input())
    build = list(map(int,input().split()))
    ans = 0
    for i in range(2,N-2):
        temp = build[i-2:i]+build[i+1:i+3]
        mt = max(temp)
        if mt<build[i]:
            ans+=build[i]-mt
    print(f'#{tc} {ans}')