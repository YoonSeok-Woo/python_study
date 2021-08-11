TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    apples = [0]+list(map(int,input().split()))
    cart = 0
    ans=0
    for i, num in enumerate(apples):
        if cart+num>=M:
            ans+=2*i
            num = num-M+cart
            cart = num%M
            ans+= 2*i*(num//M)
        else:
            cart+=num
    if apples[N-1]%M!=0:
        ans+=N*2

    print(f'#{tc} {ans}')