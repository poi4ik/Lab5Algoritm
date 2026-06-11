from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


def right_view(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:
                result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

"""""
root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
root.right.left = TreeNode(2)
"""""

"""""
root = TreeNode(3)
root.left = TreeNode(6)
root.right = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(8)
"""""

print("Preorder:", preorder(root))
print("Inorder:", inorder(root))
print("Postorder:", postorder(root))
print("Level order:", level_order(root))
print("Right view:", right_view(root))