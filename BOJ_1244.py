N = int(input())
switches = list(map(int, input().split()))
students = int(input())
for _ in range(students) :
    gender,number = map(int,input().split())
    
    if gender==1 :
        for i in range(number-1,N,number) :
            switches[i] = not switches[i]

        
    else :
        right = number
        left = number-2
        switches[number-1] = not switches[number-1]
        while left>=0 and right<N and switches[right]==switches[left] :
            switches[right] = not switches[right]
            switches[left] = not switches[left]
            right+=1
            left-=1
for i in range(N) :
    if i%20==0 and i!=0 :
        print()
    print(int(switches[i]),end=' ')
    