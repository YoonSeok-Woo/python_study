def checking(nums, i, s, nsum):
    if i>=s:
        return False
    if nsum+nums[i]==0:
        return True
    else:
        return checking(nums,i+1,s,nsum+nums[i]) or checking(nums,i+1,s,nsum)

TC = int(input())
for tc in range(1,TC+1):
    nums = list(map(int,input().split()))
    s = len(nums)
    if checking(nums,0,s,0):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')