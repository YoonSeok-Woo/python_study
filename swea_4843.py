TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    arr = list(map(int,input().split()))
    for i in range(N):
        if i%2:
            front = 101
        else:
            front = 0
        f_ind = -1
        for j in range(i,N):
            if i%2:
                if front >arr[j]:
                    front = arr[j]
                    f_ind = j
            else:
                if front < arr[j]:
                    front = arr[j]
                    f_ind = j
        if i != f_ind:
            arr[i], arr[f_ind] = arr[f_ind], arr[i]
    print(f'#{tc}',end=' ')
    for i in range(10):
        print(arr[i],end=' ')
    print()
