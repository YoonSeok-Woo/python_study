ntos = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
TC = int(input())
for _ in range(TC):
    tc, numi = input().split()
    counting = [0]*10
    nums = list(input().split())
    for i in nums:
        if i == 'ZRO':
            counting[0]+=1
        elif i == 'ONE':
            counting[1]+=1
        elif i == 'TWO':
            counting[2]+=1
        elif i=='THR':
            counting[3]+=1
        elif i=='FOR':
            counting[4]+=1
        elif i=='FIV':
            counting[5]+=1
        elif i=='SIX':
            counting[6]+=1
        elif i=='SVN':
            counting[7]+=1
        elif i=='EGT':
            counting[8]+=1
        elif i=='NIN':
            counting[9]+=1
    print(tc,end=' ')
    for i,num in enumerate(counting):
        for j in range(num):
            print(ntos[i],end=' ')
    print()