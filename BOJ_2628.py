pw, ph = map(int,input().split())
N = int(input())
ver = [0]
hor = [0]
for i in range(N) :
    vh, loc = map(int,input().split())
    if vh == 0 :
        hor.append(loc)
    else :
        ver.append(loc)
hor.append(ph)
ver.append(pw)
hor.sort()
ver.sort()
vn = 0
vmax = 0
for i in ver :
    if vmax < (i-vn) :
        vmax = (i-vn)
    vn = i
hn = 0
hmax = 0
for i in hor :
    if hmax <(i-hn) :
        hmax = (i-hn)
    hn = i
#print(hor, ver)
print(hmax*vmax)