bingo = []
for i in range(5):
    bingo.append(list(map(int,input().split())))
countx = [0]*5#0~4열까지 각열에서 몇개의 숫자가 불렸는지 체크
county = [0]*5#0~4행까지 각 행에서 몇개의 숫자가 불렸는지 체크
countcr = [0]*2#각 대각선에서 몇개의 숫자가 불렸는지 체크
bingos = 0#빙고가 몇개나왔는지
nums = [list(map(int,input().split())) for i in range(5)]
ans = 0
for line in nums:
    for n in line:
        ans+=1#몇번째 숫자인가
        for i, bl in enumerate(bingo):
            for j, num in enumerate(bl):
                if num == n:
                    countx[i]+=1#세로빙고
                    county[j]+=1#가로빙고
                    if i==j:#대각선 오.아
                        countcr[0]+=1
                    if i+j==4:#대각선 오.위
                        countcr[1]+=1
                    if countx[i]==5:#해당 열 5개가 다 체크됐다면
                        bingos+=1
                        countx[i]=100#혹시 또 세줄까봐
                    if county[j]==5:#해당 행 5개가 다 체크 됐다면
                        bingos+=1
                        county[j]=100#혹시 또 세줄까봐
                    if countcr[0]==5:#대각선 빙고 완성
                        bingos+=1
                        countcr[0]=100
                    if countcr[1]==5:#대각선 빙고 완성
                        bingos+=1
                        countcr[1]=100
        if bingos>=3:#빙고가 3개가 넘어간다면
            print(ans)#출력
            break#빠져나오기
    if bingos>=3:
        break



