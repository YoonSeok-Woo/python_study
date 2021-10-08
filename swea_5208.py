TC = int(input())

def dfs(battery,now,count):
    global answer
    if count >=answer:
        return
    if now+battery >= station[0]:
        #print(battery, now, station[0])
        answer= min(answer,count)
        return
    for i in range(now+1, now+battery+1):
        dfs(station[i],i,count+1)

for tc in range(1,TC+1):
    answer = 987654321
    station = list(map(int,input().split()))
    goal = station[0]
    battery = station[1]
    #print(answer)
    dfs(battery,1,0)
    print(f'#{tc} {answer}')
