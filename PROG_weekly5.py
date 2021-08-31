def solution(word):
    answer = 0
    char = {'A':0,'E':1,'I':2,'O':3,'U':4}
    dig = 781
    for i in word:
        answer+= 1+char[i]*dig;
        dig = (dig-1)//5
        
    return answer