# 트리 순회
# 실버 1

n = int(input())
# ord('A') = 65
tree = [[-1, -1] for _ in range(n)]

for i in range(n):
    node, child0, child1 = input().split()
    if child0 != '.':
        tree[ord(node) - ord('A')][0] = ord(child0) - ord('A')
    if child1 != '.':
        tree[ord(node) - ord('A')][1] = ord(child1) - ord('A')

def preorder(node):
    print(chr(node + ord('A')), end='')
    if tree[node][0] >= 0:
        preorder(tree[node][0])
    if tree[node][1] >= 0:
        preorder(tree[node][1])

def inorder(node):
    if tree[node][0] >= 0:
        inorder(tree[node][0])
    print(chr(node + ord('A')), end='')
    if tree[node][1] >= 0:
        inorder(tree[node][1])

def postorder(node):
    if tree[node][0] >= 0:
        postorder(tree[node][0])
    if tree[node][1] >= 0:
        postorder(tree[node][1])
    print(chr(node + ord('A')), end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)

