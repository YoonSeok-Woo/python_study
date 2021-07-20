T = int(input())
for _ in range(T) :
    K,N,M = map(int,input().split())
    stop_num = list(map(int,input().split()))
    now_location = 0
    count = 0
    i = 0
    while now_location+K<N :
        
        count+=1
        while i<M and now_location+K >= stop_num[i] :
            i+=1
        
        #print(i)
        now_location = stop_num[i-1]
        if i<M and now_location+K <stop_num[i] :
            print('#%d %d' %(_+1, 0))
            break
        if i==M and now_location+K<N :
            print('#%d %d' %(_+1, 0))
            break
        
    else :
        print('#%d %d' %(_+1, count))