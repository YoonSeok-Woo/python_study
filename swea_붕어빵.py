TC = int(input())
for tc in range(1,TC+1):
    N,M,K = map(int,input().split())
    customer = list(map(int,input().split()))
    customer.sort()
    print(f'#{tc}',end = ' ')
    for i,time in enumerate(customer):
        if (time//M)*K < i+1:
            print("Impossible")
            break
    else:
        print("Possible")
