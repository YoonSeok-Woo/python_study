TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    ans = True
    for i in range(N):
        if M <=0:
            ans = False
            break
        if M%2==0:
            ans = False
            break
        M= M//2
    if ans:
        answer = 'ON'
    else:
        answer = 'OFF'
    print(f'#{tc} {answer}')
