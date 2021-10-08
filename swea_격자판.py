TC = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(i,j,num):
    if len(num)==7:
        answer.add(num)
        return
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        if ni <0 or nj <0 or ni >=4 or nj >=4:
            continue
        dfs(ni,nj,num+str(board[ni][nj]))

for tc in range(1,TC+1):
    answer = set()
    board = [list(map(int,input().split())) for i in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(i,j,str(board[i][j]))
    print(f'#{tc} {len(answer)}')
