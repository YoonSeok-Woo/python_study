TC = int(input())
for tc in range(1,TC+1):
    ans = True
    N, M = map(int,input().split())
    wall = list(list(input()) for i in range(N))
    for i in range(N):
        for j in range(M):
            if wall[i][j] == '#':
                if i+1>=N or j+1>=M:
                    ans = False
                    break
                if wall[i+1][j]=='.' or wall[i][j+1]=='.' or wall[i+1][j+1]=='.':
                    ans = False
                    break
                else:
                    wall[i][j] = '.'
                    wall[i+1][j]='.'
                    wall[i][j+1]='.'
                    wall[i+1][j+1]='.'
        if not ans:
            break
    if ans:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')