TC = int(input())
for tc in range(1,TC+1):
    print(f'#{tc}',end=' ')
    N = int(input())
    blocks = list(map(int,input().split()))
    ans = list(x for x in range(N-1,-1,-1))
    #print(ans)
    for i, num in enumerate(blocks):
        for j in range(i+1,N):
            if num<=blocks[j]:
                ans[i]-=1
    print(max(ans))