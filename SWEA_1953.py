from queue import Queue
visit = []
ug = []
pipe = [
    [],
    [[1,0],[-1,0],[0,1],[0,-1]],
    [[1,0],[-1,0]],
    [[0,1],[0,-1]],
    [[-1,0],[0,1]],
    [[1,0],[0,1]],
    [[1,0],[0,-1]],
    [[-1,0],[0,-1]]
]
def bfs(y,x,N,M,L):
    q = Queue()
    global visit
    global ug
    global pipe
    visit[y][x] = True
    count=1
    q.put([y,x,0])
    while not q.empty():
        temp= q.get()
        #print(temp)
        y = temp[0]
        x = temp[1]
        l = temp[2]
        p_shape = pipe[ug[y][x]]
        for i in p_shape:
            ny = y+i[0]
            nx = x+i[1]
            nl = l+1
            if ny < 0 or ny >=N or nx <0 or nx>=M:
                continue
            if i[0]==1 and (ug[ny][nx]==3 or ug[ny][nx]==5 or ug[ny][nx]==6):
                continue
            if i[0]==-1 and (ug[ny][nx]==3 or ug[ny][nx]==4 or ug[ny][nx]==7):
                continue
            if i[1]==1 and (ug[ny][nx]==2 or ug[ny][nx]==4 or ug[ny][nx]==5):
                continue
            if i[1]==-1 and (ug[ny][nx]==2 or ug[ny][nx]==6 or ug[ny][nx]==7):
                continue
            if visit[ny][nx] or ug[ny][nx]==0 or nl >= L:
                continue
            visit[ny][nx]=True
            count+=1
            q.put([ny,nx,nl])
    return count


TC = int(input())

for tc in range(TC):
    count = 0
    N,M,R,C,L = map(int,input().split())
    visit = [[False]*M for i in range(N)]
    temp = []
    for i in range(N):
        temp.append(list(map(int,input().split())))
    ug = temp
    del temp
    print(f'#{tc+1} {bfs(R,C,N,M,L)}')

    
