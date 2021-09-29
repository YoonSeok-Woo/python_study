TC = int(input())
pattern = [
    [3,2,1,1],
    [2,2,2,1],
    [2,1,2,2],
    [1,4,1,1],
    [1,1,3,2],
    [1,2,3,1],
    [1,1,1,4],
    [1,3,1,2],
    [1,2,1,3],
    [3,1,1,2],
]
def ctoi(code):
    checker = code[0]
    patt = []
    temp = 0
    for i in code:
        if i== checker:
            temp+=1
        if i!= checker:
            patt.append(temp)
            temp = 1
            checker = 1-checker
    patt.append(temp)
    #print(patt)
    for i in range(10):
        for j in range(4):
            if patt[j] != pattern[i][j]:
                break
        else:
            return i
    return -1
def cal(inp):
    nums = []
    for i in range(8):
        #print(inp[i*7:i*7+7])
        nums.append(ctoi(inp[i*7:i*7+7]))
        #print(nums[i])
    checking = 0
    for i in range(7):
        if nums[i]==-1:
            return 0
        if i%2:
            checking += nums[i]
            #print(nums[i])
        else:
            checking += nums[i]*3
            #print(nums[i])
    checking+= nums[7]
    #print(nums, checking)
    if checking%10:
        return 0
    else:
        return sum(nums)
for tc in range(1,TC+1):
    M, N = map(int,input().split())
    inp = [0]*N
    for i in range(M):
        temp = list(map(int,input()))
        if 1 in temp:
            inp = temp

    for i in range(N-1,-1,-1):
        if inp[i]==1:
            print(f'#{tc} {cal(inp[i-55:i+1])}')
            break
    else:
        print(f'#{tc} {0}')
