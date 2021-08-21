TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    N=N//10
    dp = [0]*(N+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,N+1):
        dp[i] = dp[i-1]+dp[i-2]*2
    print(f'#{tc} {dp[N]}')