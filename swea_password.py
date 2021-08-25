for i in range(10):
    tc = int(input())
    nums = list(map(int,input().split()))
    front = 0
    back = 7
    minus = 1
    while nums[front]-minus>0:
        now = nums[front]-minus
        front+=1
        front = front%8
        back +=1
        back = back%8
        nums[back] = now
        minus=minus%5
        minus+=1
    now = nums[front]-minus
    front+=1
    front = front%8
    back+=1
    back= back%8
    nums[back] = max(0,now)
    print(f'#{tc}',end = ' ')
    for i in nums[front:]:
        print(i,end = ' ')
    for i in nums[:back+1]:
        print(i,end = ' ')
    print()
