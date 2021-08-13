TC = int(input())
for tc in range(1,TC+1):
    N, K = map(int,input().split())
    sums = [(0,0)]
    ans = 0
    for i in range(1,12+1):
        s = sums[:]
        for nums in s:
            if i+nums[0]==K and nums[1]+1==N:
                ans+=1
            sums.append((i+nums[0],nums[1]+1))
    print(f'#{tc} {ans}')