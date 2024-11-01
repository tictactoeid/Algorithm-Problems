# Closest Binary Search Tree Value II
# Hard

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, target, k):
        if node is None:
            return
        if len(self.heap) < k:
            heapq.heappush(self.heap, (-abs(target - node.val), node.val))
        else:
            heapq.heappushpop(self.heap, (-abs(target - node.val), node.val))

        # heap에 상위 k개만 남기면 되기 때문에, 길이를 k로 유지해주면 heap 연산 복잡도를 O(log k)로 유지할 수 있음

        self.dfs(node.left, target, k)
        self.dfs(node.right, target, k)

    def closestKValues_heap(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # O(nlogk)
        self.heap = []
        self.dfs(root, target, k)
        return [x[1] for x in self.heap]

    def inorder_traversal(self, node):
        if node is None:
            return
        # left - node - right
        self.inorder_traversal(node.left)
        self.elements.append(node.val)
        self.inorder_traversal(node.right)

    def get_farthest(self, target, start, end):
        s = self.elements[start]
        e = self.elements[end]

        return e if abs(s - target) < abs(e - target) else s

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.elements = []
        self.inorder_traversal(root)
        # BST의 inorder traversal은 원소들을 정렬된 순서대로 반환함

        n = len(self.elements)
        closest = bisect.bisect_left(self.elements, target)

        left = self.elements[closest - 1] if closest > 0 else math.inf
        right = self.elements[closest] if closest < n else math.inf
        closest = closest - 1 if abs(left - target) < abs(right - target) else closest

        # 가장 가까운 원소 하나를 찾고, 그 원소를 포함하는 length k의 모든 subarray들을 sliding window

        start = max(0, closest - k + 1)
        end = start + k - 1

        farthest = self.get_farthest(target, start, end)
        result = [start, end, farthest]

        while end < n and start <= closest:
            farthest = self.get_farthest(target, start, end)
            if abs(result[-1] - target) > abs(farthest - target):
                result = [start, end, farthest]
            start += 1
            end += 1
        return self.elements[result[0]:result[1] + 1]
