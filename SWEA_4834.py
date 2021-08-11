TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    nums = list(map(int,input()))
    count = [0]*10
    for i in nums:
        count[i]+=1
    mx = 0
    ind = -1
    for i , c in enumerate(count):
        if c >=mx :
            mx = c
            ind = i
    print(f'#{tc} {ind} {mx}')