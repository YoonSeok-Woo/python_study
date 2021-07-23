from itertools import combinations
shorts = []
for i in range(9) :
    shorts.append(int(input()))
shorts.sort()
res = list(combinations(shorts,7))
for i in res :
    if sum(i) == 100 :
        for j in range(7) :
            print(i[j])
        break