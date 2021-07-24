T = int(input())
for tc in range(1,T+1) :
    prices = list(map(int,input().split()))
    plan = [0]+list(map(int,input().split()))
    dp = []
    pr = []
    for i in range(13) :
        dp.append(0)
        pr.append(0)
    for i in range(13) :
        pr[i] = prices[0]*plan[i]
        pr[i] = prices[1] if prices[1] < pr[i] else pr[i]
    for i in range(1,13) :
        if i<2 :
            dp[i] = dp[i-1]+pr[i]
        else :
            dp[i] = min(dp[i-3]+prices[2],dp[i-1]+pr[i])
    print(f'#{tc} {min(dp[12],prices[3])}')
