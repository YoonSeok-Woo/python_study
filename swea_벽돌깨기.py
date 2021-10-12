TC = int(input())

def burst(i,j):
    if i<0 or j <0 or i>=H or j>=W:
        return
    if board[i][j]==0:
        return
    area = board[i][j]
    board[i][j]=0
    for k in range(1,area):
        burst(i+k,j)
        burst(i-k,j)
        burst(i,j+k)
        burst(i,j-k)

def drop(loc):
    global W
    global H

    for i in range(H):
        if board[i][loc]!=0:
            area = board[i][loc]
            burst(i,loc)
            break
    else:
        return 0
    if area<=1:
        return 1
    for i in range(W):
        temp = []
        for j in range(H):
            if board[j][i]!=0:
                temp.append(board[j][i])
                board[j][i]=0
        for j in range(H-1,-1,-1):
            if not temp:
                break
            board[j][i] = temp.pop()
    return 1

def dfs(times):
    global answer
    global board

    if times >=N:
        blocks = 0
        for i in range(H):
            for j in range(W):
                if board[i][j]!=0:
                    blocks+=1
        #if blocks == 19:
        #    for i in range(H):
        #        print(board[i])
        answer=min(answer,blocks)
        return
    temp = [board[j][:] for j in range(H)]
    for i in range(W):
        drop(i)
        dfs(times+1)
        board = [temp[j][:] for j in range(H)]


for tc in range(1,TC+1):
    N, W, H = map(int,input().split())
    answer = 987654321
    board = [list(map(int,input().split())) for i in range(H)]
    dfs(0)

    print(f'#{tc} {answer}')