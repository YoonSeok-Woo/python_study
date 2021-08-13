T = int(input())
for tc in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    price = price[::-1]
    now = price[0]
    ans = 0
    for i, p in enumerate(price):
        if i == 0:
            continue
        if now <p:
            now = p
        else :
            ans+=now-p
    print('#{} {}'.format(tc,ans))