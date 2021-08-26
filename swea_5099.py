from queue import Queue

TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int,input().split())
    pizza = list(map(int,input().split()))
    oven = Queue()
    pnum = -1
    for i, piz in enumerate(pizza):
        if oven.qsize()>=N:
            pnum = i+1
            break
        else:
            oven.put((i+1,piz))
    ans = -1
    while not oven.empty():
        now, cheeze = oven.get()
        if cheeze//2 !=0:
            oven.put((now,cheeze//2))
        else:
            if pnum>len(pizza):
                ans = now
                continue
            else:
                ans = now
                oven.put((pnum,pizza[pnum-1]))
                pnum+=1
    print(f'#{tc} {ans}')
