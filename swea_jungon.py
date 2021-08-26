TC = int(input())
def checking(n):
    ans = n
    now = n%10
    n = n//10
    while n>0:
        #print(now, n)
        if now < n%10:
            return -1
        now = n % 10
        n = n // 10
    return ans
for tc in range(1,TC+1):
    N =int(input())
    A = list(map(int,input().split()))
    ans = -1
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,checking(A[i]*A[j]))
    print(f"#{tc} {ans}")