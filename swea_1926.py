N = int(input())
def sam69(num): #숫자를 받으면 출력할 문자로 바꿔주는 함수
    res = ''
    n = num
    while n>0:
        if (n%10)==0:
            pass
        elif (n%10)%3==0:#3 6 9 가 나오면 -를 추가해주고
            res+='-'
        n=n//10
    if res:#res 길이가 0이아니면 -하나라도 있으면
        return res
    else:
        return num
for i in range(1,N+1):
    print(f'{sam69(i)}',end = ' ')