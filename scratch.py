
#import sys

#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    s = len(array)
    for i in range(s):
        for j in range(s-i-1):
            if array[j]>array[j+1]:
                (array[j], array[j+1]) = (array[j+1],array[j])
    print(f'#{test_case}',end=' ')
    for num in array:
        print(num, end=' ')
    print()