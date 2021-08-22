N,K = map(int,input().split())
students = [[0]*7 for i in range(2)]
ans = 0
for i in range(N):
    i, j  = map(int,input().split())
    students[i][j]+=1
    if students[i][j]==1:#학년별 방을 하나씩 배정할떄마다
        ans+=1
    if students[i][j]==K:#방이 꽉찼으면 다음방으로
        students[i][j]=0
print(ans)