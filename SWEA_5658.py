
def cal(n) :
    l = len(n)
    l-=1
    res = 0
    for c in n :
        if c>='0' and c <= '9' :
            a = int(c)
        else :
            a = ord(c)-ord('A')+10
        res+=a*(16**l)
        l-=1
    return res

TC = int(input())
for tc in range(1,TC+1) :
    N, K = map(int, input().split())
    nums = input()
    nums = nums*2
    iter = int(N/4)
    keys = []
    for i in range(iter) :
        keys.append(cal(nums[i:iter+i]))
        keys.append(cal(nums[iter+i:iter*2+i]))
        keys.append(cal(nums[iter*2+i:iter*3+i]))
        keys.append(cal(nums[iter*3+i:iter*4+i]))
    keys.sort()
    s = len(keys)
    count = 1
    now = 0
    for i in range(s-1,-1,-1) :
        if(count == K) :
            print(f'#{tc} {keys[i]}')
            break
        if(keys[i]==now):
            pass
        
        else :
            count +=1
        now = keys[i]
    
