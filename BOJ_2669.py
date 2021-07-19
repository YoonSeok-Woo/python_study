# 전체 영역
area = [[0]*101 for _ in range(101)]
# 직사각형의 너비
count = 0
for i in range(4) :
    
    x1, y1, x2, y2 = map(int, input().split())
    #입력받은 직사각형을 칠해주자
    for j in range(x1,x2) :
        for k in range(y1,y2) :
            #칠해진 면적이 아닐 경우(area[j][k]==0) 칠하고 직사각형 너비를 하나 더해준다 
            if area[j][k] == 0 :
                area[j][k] = 1
                count +=1
#출력
print(count)
    