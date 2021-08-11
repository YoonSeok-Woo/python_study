T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    mx = nums[0]
    mn = nums[0]
    for i in nums:
        if mx < i:
            mx = i
        if mn > i:
            mn = i
    print(f'#{tc} {mx-mn}')