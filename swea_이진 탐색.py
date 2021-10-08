TC = int(input())
def binary_search(nums, t):
    l = 0
    r = len(nums)-1
    inc = 0
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==t:
            return True
        elif nums[mid] < t:
            if inc == 1:
                return False
            l = mid + 1
            inc = 1
        else:
            if inc == -1:
                return False
            r = mid - 1
            inc = -1
    #print(t)
    return False

for tc in range(1,TC+1):
    la, lb = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in B:
        if binary_search(A,i):
            #print(i)
            ans+=1
    print(f'#{tc} {ans}')