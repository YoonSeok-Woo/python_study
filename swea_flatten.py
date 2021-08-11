TC = 10
for i in range(1,TC+1):
    N = int(input())
    boxes = list(map(int,input().split()))
    boxes.sort()
    sum_box = sum(boxes)
    avg_box = sum(boxes)//100

    if sum_box%100==0:
        ans = 0
    else:
        ans = 1
    l = 0
    r = 99
    moves = []
    tN=N
    flag = False
    rem = 0
    while tN>0:
        if boxes[r]<=avg_box:
            print(ans)
            flag = True
            break
        move = (boxes[r]-boxes[r-1])*(100-r)
        if tN<move:
            rem = tN//(100-r)
            break
        else:
            r-=1
            tN-=move
    top = boxes[r]-rem
    tN=N
    rem  = 0
    while tN>0:
        if flag:
            break
        stacking = (boxes[l+1]-boxes[l])*(l+1)
        if tN<stacking:
            rem = tN//(l+1)
            break
        else:
            l+=1
            tN-=stacking
    bottom = boxes[l]+rem
    if not flag:
        print(f'#{i} {top-bottom}')
