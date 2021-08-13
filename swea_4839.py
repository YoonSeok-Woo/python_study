TC = int(input())
for tc in range(1,TC+1):
    P, A, B = map(int,input().split())
    la = 1
    lb = 1
    ra = P
    rb = P
    ca = 0
    cb = 0
    while la<=ra:
        ma = (la+ra)//2
        ca+=1
        if ma==A:
            break
        elif ma>A:
            ra=ma
        elif ma<A:
            la=ma
    while lb<=rb:
        mb = (lb+rb)//2
        cb+=1
        if mb == B:
            break
        elif mb>B:
            rb = mb
        elif mb<B:
            lb = mb

    if ca == cb :
        ans = 0
    elif ca>cb:
        ans = 'B'
    elif ca<cb:
        ans = 'A'

    print(f'#{tc} {ans}')