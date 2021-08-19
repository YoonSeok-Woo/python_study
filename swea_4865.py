TC = int(input())
for tc in range(1,TC+1):
    str1 = input()
    str2 = input()
    alph = dict()
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in alphabets:
        alph[i] = 0
    for i in str2:
        alph[i]+=1
    ans = 0
    for i in str1:
        if alph[i]>ans:
            ans = alph[i]
    print(f'#{tc} {ans}')