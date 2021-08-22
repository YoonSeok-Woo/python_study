money = [50000,10000,5000,1000,500,100,50,10]
TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    ans = [0]*8
    for i in range(8):
        ans[i]+= N//money[i]
        N%=money[i]
    print(f'#{tc}')
    for i in range(8):
        print(f'{ans[i]}',end=' ')
    print()