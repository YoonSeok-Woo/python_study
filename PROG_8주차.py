def solution(sizes):
    answer = 0
    maxmax = 0
    minmax = 0
    for i in sizes:
        maxmax = max(max(i),maxmax)
        minmax = max(min(i),minmax)
    answer = minmax*maxmax
    return answer