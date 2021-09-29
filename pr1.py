TC = int(input())
for tc in range(1,TC+1):
    arr = list(map(int,input()))
    ans = []
    temp = 0
    for i in range(len(arr)):
        if i%7==0:
            if i !=0:
                ans.append(temp)
            temp = 0
        temp+=arr[i]*2**(7-i%7-1)
    ans.append(temp)
    print(f'#{tc}',end = ' ')
    for i in ans:
        print(i, end = ' ')
    print()