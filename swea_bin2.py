nums = [1/2**x for x in range(13)]
TC = int(input())
for tc in range(1,TC+1):
    target = float(input())
    answer = ''
    temp = 0.0
    for i in range(1,13):
        if temp + nums[i] <=target:
            answer+='1'
            temp +=nums[i]
        else:
            answer+='0'
        if temp == target:
            break
    else:
        answer = 'overflow'
    print(f'#{tc} {answer}')