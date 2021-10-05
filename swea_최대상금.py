TC = int(input())
def swap(num):
    global answer
    if num == 0 :
        answer = max(answer,int(''.join(target)))
        return
    l = len(target)
    for i in range(l):
        for j in range(i+1,l):
            target[i], target[j] = target[j], target[i]
            #print(''.join(target))
            if not (''.join(target)+str(num-1)) in visited:
                visited.add(''.join(target)+str(num-1))
                swap(num-1)
            else:
                if (num-1)%2:
                    target[l-1],target[l-2] = target[l-2],target[l-1]
                answer = max(answer,int(''.join(target)))
                if (num-1)%2:
                    target[l-1],target[l-2]=target[l-2],target[l-1]
            target[i], target[j] = target[j],target[i]
for tc in range(1,TC+1):
    answer = 0
    visited = set()
    target, num = input().split()
    num = int(num)
    target = list(target)
    swap(num)
    print(f'#{tc} {answer}')