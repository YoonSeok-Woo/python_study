TC = int(input())
for tc in range(1,TC+1):
    N = int(input())#N 이 100까지 올 수 있어서 원소가 100개의 부분집합이 10^30
    nums = list(map(int,input().split()))
    ans = [0]#
    added = [False]*(sum(nums)+1) #0부터 모든 합계까지 ans에 더해졌는지 여부를 체크하는 added 를 만들고
    added[0] = True#0은 기본적으로 포함이니까
    for i in nums:
        l = len(ans)#현재까지 ans를 돌아보면서
        for j in range(l):#각 넘버들을 더한 값들을
            temp = i+ans[j]
            if added[temp]:#들어있는지 체크하고 들어있으면 넘어가고
                continue
            added[temp]=True#아니면 ans에 추가해줍니다.
            ans.append(temp)
    #ans에 모든 경우의 수가 추가가 되었을 테니까
    print(f'#{tc} {len(ans)}')#ans의 길이를 출력하면 됩니다.
