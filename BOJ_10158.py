w, h = map(int,input().split())
x, y = map(int,input().split())
t = int(input())
x = t+x
y = t+y
if (x//w)%2 :
    x = w- x%w
else :
    x = x%w
if (y//h)%2 :
    y = h-y%h
else :
    y = y%h

print(x, y)