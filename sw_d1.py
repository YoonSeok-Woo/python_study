
#import sys

#sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    bs = list(map(int, input().split()))
    count = 0
    for i, h in enumerate(bs):
        if i < 2 or i > N-3:
            continue
        top = 0
        for j in range(-2, 3):
            if (not j) and top < bs[i+j]:
                top = bs[i+j]
        if top < h:
            count += h-top
    print(f'#{test_case} {count}')