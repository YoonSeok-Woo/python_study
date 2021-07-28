N = int(input())
board = list(list(-1 for i in range(1001)) for i in range(1001))
papers = []
ans = list(0 for i in range(N))
for _ in range(N):
    paper = list(map(int,input().split()))
    for i in range(paper[3]):
        for j in range(paper[2]):
            ind_i = i+paper[1]
            ind_j = j+paper[0]
            temp = board[ind_i][ind_j]
            if temp!=-1:
                ans[temp]-=1
            board[ind_i][ind_j] = _
            ans[_] +=1
            
    papers.append(paper)
for i in range(N):
    print(ans[i])