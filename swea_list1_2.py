TC = int(input())
for tc in range(1,TC+1):
    nums = list(map(int,input().split()))
    s = len(nums)
    i = 0
    ans = False
    sums = [0]
    for i in nums:
        if ans:
            break
        l = len(sums)
        for j in range(l):
            if i+sums[j]==0:
                ans = True
                break
            sums.append(i+j)
    if ans :
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')