TC = int(input())
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    strings = []
    for i in range(N):
        strings.append(input())
    found = False
    ans = ''
    for i in range(N-M+1):#세로 회문부터 찾자
        for j in range(N):
            text = ''
            for k in range(M):
                text+=strings[i+k][j]
            t_rev = text[::-1]
            if text == t_rev:
                ans = text
                found = True
                break
        if found :
            break
    found = False
    for i in range(N):
        for j in range(N-M+1):
            text = ''
            for k in range(M):
                text+=strings[i][j+k]
            t_rev = text[::-1]
            if text == t_rev:
                ans=text
                found = True
                break
        if found:
            break
    print(f'#{tc} {ans}')
