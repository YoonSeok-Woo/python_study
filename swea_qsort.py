TC = int(input())
def qsort(l,r):
    if l>=r:
        return
    p = l
    i = l+1
    j = r-1
    while i <=j:
        while i<=j and nums[p] >=nums[i]:
            i+=1
        while i<=j and nums[p] <=nums[j]:
            j-=1
        if i <=j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[p], nums[j] = nums[j],nums[p]
    qsort(l,j)
    qsort(j+1,r)


for tc in range(1,TC+1):
    N = int(input())
    nums = list(map(int,input().split()))
    l = 0
    r = len(nums)
    qsort(l,r)
    print(f'#{tc} {nums[N//2]}')