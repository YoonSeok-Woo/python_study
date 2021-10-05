from collections import deque
TC = int(input())
dx = [1,0]
dy = [0,1]
for tc in range(1,TC+1):
    N = int(input())
    sums = [[0]*N for i in range(N)]
    nums = [list(map(int,input().split())) for i in range(N)]
    q = deque()
    q.append((0,0))
    sums[0][0] = nums[0][0]
    while q:
        i, j = q.popleft()
        for k in range(2):
            ni = i+dx[k]
            nj = j+dy[k]
            if ni >=N or nj >=N:
                continue
            if sums[ni][nj]!=0 and sums[i][j] + nums[ni][nj] > sums[ni][nj]:
                continue
            sums[ni][nj] = sums[i][j]+nums[ni][nj]
            q.append((ni,nj))
    print(f'#{tc} {sums[N-1][N-1]}')