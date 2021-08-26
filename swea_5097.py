TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    q = list(map(int,input().split()))
    i = 0
    for j in range(M):
        i+=1
        i=i%N
    print(f'#{tc} {q[i]}')