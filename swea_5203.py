TC = int(input())
for tc in range(1,TC+1):
    player1 = [0]*10
    player2 = [0]*10
    nums = list(map(int,input().split()))
    ans = 0
    for i , num in enumerate(nums):
        if i %2:
            player2[num]+=1
            if player2[num]>=3:
                ans = 2
                break
            for k in range(num-2,num+1):
                for j in range(3):
                    if k+j >= 10 or k+j <0:
                        break
                    if player2[k+j]==0:
                        break
                else:
                    ans = 2
                    break
            if ans:
                break
        else:
            player1[num]+=1
            if player1[num] >=3:
                ans = 1
                break
            for k in range(num-2,num+1):
                for j in range(3):
                    if k+j >= 10 or k+j <0:
                        break
                    if player1[k+j]==0:
                        break
                else:
                    ans = 1
                    break
            if ans:
                break
    #print(player1)
    #print(player2)
    print(f'#{tc} {ans}')