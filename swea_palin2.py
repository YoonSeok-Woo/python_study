def palin(strings, M):
    if M==1:
        return True
    for i in range(100 - M + 1):  # 세로 회문부터 찾자
        for j in range(100):
            text = ''
            for k in range(M):
                text += strings[i + k][j]
            t_rev = text[::-1]
            if text == t_rev:
                return True

    for i in range(100):
        for j in range(100 - M + 1):
            text = ''
            for k in range(M):
                text += strings[i][j + k]
            t_rev = text[::-1]
            if text == t_rev:
                return True
    return False

for _ in range(10):
    tc = int(input())
    board = []
    for i in range(100):
        board.append(input())
    ans = 0
    for i in range(100, 1,-1):
        if palin(board,i):
            print(f'#{tc} {i}')
            break
