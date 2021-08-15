N= int(input())
tree = list([] for i in range(26))
for i in range(N):
    p, c1,c2 = input().split()
    tree[ord(p)-ord('A')].append(ord(c1)-ord('A'))
    tree[ord(p)-ord('A')].append(ord(c2)-ord('A'))

def preorder(root):#전위
    print(chr(root+ord('A')), end = '') #확인
    if tree[root][0]!=ord('.')-ord('A'):#왼쪽
        preorder(tree[root][0])
    if tree[root][1]!=ord('.')-ord('A'):#오른쪽
        preorder(tree[root][1])

def inorder(root):#중위
    if tree[root][0]!=ord('.')-ord('A'):#왼쪽
        inorder(tree[root][0])
    print(chr(root+ord('A')),end = '')  #확인
    if tree[root][1]!=ord('.')-ord('A'):#오른쪽
        inorder(tree[root][1])

def postorder(root):#후위
    if tree[root][0]!=ord('.')-ord('A'): #왼쪽 if문은 자식이 없는 경우
        postorder(tree[root][0])
    if tree[root][1]!=ord('.')-ord('A'):#오른쪽
        postorder(tree[root][1])
    print(chr(root+ord('A')),end='')    #확인

preorder(0)
print()
inorder(0)
print()
postorder(0)
for i in tree:
    print(i)