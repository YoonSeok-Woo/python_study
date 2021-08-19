TC = int(input())

for tc in range(1, TC+1):
    pattern = input()
    target = input()
    lp = len(pattern)
    lt = len(target)
    ans = 0
    for i in range(lt-lp+1):
        for j in range(lp):
            if pattern[j] != target[i+j]:
                break
        else:
            ans = 1
            break
    print(f'#{tc} {ans}')