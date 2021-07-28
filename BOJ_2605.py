N = int(input())
line =[]
students = list(map(int,input().split()))
for i in range(1,N+1):
    s_i = i-1
    line.insert(s_i-students[s_i],i)
for i in range(N):
    print(line[i],end=' ')