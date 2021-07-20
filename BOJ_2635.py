N = int(input())
target = 0
ans = 0
for i in range(N,-1,-1) :
    
    a2 = N
    a1 = i
    a0 = N-i
    count = 2
    while(a2-a1>=0) :
        count +=1
        a2 = a1
        a1 = a0
        a0 = a2-a1
    if count> ans :
        ans = count
        target = i
    
print(ans)
a2 = N
a1 = target
a0 = a2-a1
print(a2, end = ' ')
print(a1, end = ' ')

while a2-a1>=0 :
    print(a0, end = ' ')
    a2 = a1
    a1 = a0
    a0 = a2-a1
    
