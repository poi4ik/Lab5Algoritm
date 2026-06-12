# # Лабораторная работа 5

Тема:  Обход бинарного дерева

Выполнил Пехтерев Иван Игоревич, группа ИДБ-25-07

Базовая задача: Реализовать функции:
-   `preorder(root)`,  `inorder(root)`,  `postorder(root)`: прямой, симметричный и обратный обходы, возвращающие список значений.
-   `level_order(root)`: обход в ширину (BFS), выводящий элементы по уровням.
-   Создать несколько тестовых деревьев для проверки работы функций.

Вариативная часть: 
 -  Вывести правый вид» дерева (последний узел на каждом уровне).


# Импорт 

`from collections import deque`

## Класс дерева
```
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```
## Preorder - прямой обход
```
def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)

```
## Inorder - симметричный обход
```
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

```
## Postorder - обратный обход
```
def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]

```
## Level order - обход по уровням
```
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

```

# Right view - правый вид дерева
Функция выводит крайние правые узлы каждого этажа
```
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
```
## Деревья
Дерево №1
```
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
```
```
        1
      /   \
     2     3
    / \     \
   4   5     6
   ```
   Дерево №2
   ```
   root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
root.right.left = TreeNode(2)
```
```
          6
        /   \
       4     8
      / \   / \
     1   4 2   7
```
Дерево №3
```
root = TreeNode(3)
root.left = TreeNode(6)
root.right = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(8)
```
```
        3
      /   \
     6     1
      \     \
       6     8
```
## Вывод результата
```
print("Preorder:", preorder(root))  
print("Inorder:", inorder(root))  
print("Postorder:", postorder(root))  
print("Level order:", level_order(root))  
print("Right view:", right_view(root))
```
## Примеры вывода:
Дерево №1

```
Preorder: [1, 2, 4, 5, 3, 6]
Inorder: [4, 2, 5, 1, 3, 6]
Postorder: [4, 5, 2, 6, 3, 1]
Level order: [[1], [2, 3], [4, 5, 6]]
Right view: [1, 3, 6]
```
Дерево №2
```
Preorder: [6, 4, 1, 4, 8, 2, 7]
Inorder: [1, 4, 4, 6, 2, 8, 7]
Postorder: [1, 4, 4, 2, 7, 8, 6]
Level order: [[6], [4, 8], [1, 4, 2, 7]]
Right view: [6, 8, 7]
```
Дерево №3
```
Preorder: [3, 6, 6, 1, 8]
Inorder: [6, 6, 3, 1, 8]
Postorder: [6, 6, 8, 1, 3]
Level order: [[3], [6, 1], [6, 8]]
Right view: [3, 1, 8]
```
