from collections import deque
N = int(input())
board = [list(map(int,input())) for i in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            count = 1
            q = deque()
            q.append((i,j))
            board[i][j] = 0
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if nx < 0 or ny<0 or nx>=N or ny>=N:
                        continue
                    if board[nx][ny]==0:
                        continue
                    q.append((nx,ny))
                    board[nx][ny] = 0
                    count+=1
            ans.append(count)
ans.sort()
print(len(ans))
for i in ans:
    print(i)