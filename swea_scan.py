import sys
sys.stdin = open("input.txt","r")
TC = int(input())
htob= {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}
cton = {
    '211': 0,
    '221':1,
    '122':2,
    '411':3,
    '132':4,
    '231':5,
    '114':6,
    '312':7,
    '213':8,
    '112':9
}
def valid(nums):
    checker = 0
    for i in range(8):
        if i%2:
            checker+=nums[i]
        else:
            checker+=nums[i]*3
    if (checker)%10:
        return 0
    else:
        return sum(nums)
for tc in range(1,TC+1):
    N, M = map(int,input().split())
    code = [input() for x in range(N)]
    ans = 0
    ansset = []
    for i in range(N):
        temp = ''
        for j in range(M):
            temp += htob[code[i][j]]
        temp
        j = 4*M-1
        #print(code[i])
        #print(temp[:j+1])
        
        while '1' in temp[:j+1]:
            #print(temp[:j+1])
            nums = [0]*8
            code_ind = 7
            while temp[j]=='0':
                if j<0:
                    break
                j-=1
            for i in range(8):
                n1,n2,n3 = 0,0,0
                while temp[j]=='1':
                    n3+=1
                    j-=1
                while temp[j]=='0':
                    n2+=1
                    j-=1
                while temp[j] == '1':
                    n1+=1
                    j-=1
                while temp[j]=='0':
                    if j<0:
                        break
                    j-=1
                base = min(n1,n2,n3)
                #print(n1,n2,n3)
                n1, n2, n3 = n1//base,n2//base,n3//base
                t_key = str(n1)+str(n2)+str(n3)
                nums[code_ind] = cton[t_key]
                code_ind-=1
            
            val = valid(nums)
            #if tc==2:
            #    print(nums,val)
            
            if not nums in ansset :
                ansset.append(nums)
                ans += val
            
    print(f'#{tc} {ans}')
    
    
