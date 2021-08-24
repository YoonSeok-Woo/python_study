TC = int(input())
def win(a,b):
    if nums[a]==1:
        if nums[b]==1:
            return min(a,b)
        elif nums[b]==2:
            return b
        elif nums[b]==3:
            return a
    if nums[a]==2:
        if nums[b]==2:
            return min(a,b)
        elif nums[b]==3:
            return b
        elif nums[b]==1:
            return a
    if nums[a]==3:
        if nums[b]==3:
            return min(a,b)
        elif nums[b]==1:
            return b
        elif nums[b]==2:
            return a

def tm(i,j):
    if i==j:
        return i
    else:
        return win(tm(i,(i+j)//2),tm((i+j)//2+1,j))

for tc in range(1,TC+1):
    N = int(input())
    nums = list(map(int,input().split()))
    print(f'#{tc} {tm(0,N-1)+1}')