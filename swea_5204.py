TC = int(input())
def merge(a,b):
    global count
    if a[-1] > b[-1]:
        count+=1
    i = 0
    j = 0
    a+=[100000001]
    b+=[100000001]
    res = []

    while i < len(a)-1 or j<len(b)-1:
        if a[i] <= b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    return res
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    l = 0
    r = len(arr)
    return merge(merge_sort(arr[l:r//2]),merge_sort(arr[r//2:r]))


for tc in range(1,TC+1):
    N = int(input())
    count = 0
    nums = list(map(int,input().split()))
    res = merge_sort(nums)
    print(f'#{tc} {res[N//2]} {count}')