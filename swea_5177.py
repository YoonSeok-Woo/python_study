TC = int(input())
def heap_push(n):
    heap.append(n)
    now = len(heap)-1
    if now<=1:
        return 1
    while heap[now]<heap[now//2]:
        heap[now],heap[now//2] = heap[now//2],heap[now]
        now = now//2
    return now
for tc in range(1,TC+1):
    N = int(input())
    nums = list(map(int,input().split()))
    heap = [0]
    now = 0
    ans = 0
    for num in nums:
        heap_push(num)
    now = len(nums)
    while now//2 > 0:
        ans += heap[now//2]
        now = now//2
    print(heap)
    print(f'#{tc} {ans}')