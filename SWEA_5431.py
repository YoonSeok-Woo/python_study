TC = int(input())
for tc in range(1,TC+1):
    N, K = map(int,input().split())
    submit = list(map(int,input().split()))
    check = [False]*(N+1)
    for i in submit:
        check[i]=True
    print(f'#{tc}',end= ' ')
    for i in range(1,N+1):
        if not check[i]:
            print(f'{i}',end = ' ')
    print()