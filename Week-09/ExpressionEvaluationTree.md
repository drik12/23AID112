# 🌳 Expression Evaluation using Trees

Expression trees are a **binary tree representation of expressions** where:
- **Leaves** = operands (numbers/variables)  
- **Internal nodes** = operators (`+`, `-`, `*`, `/`, etc.)

---

## 🧩 Example Expression Tree

Example expression:  
`(3 + 5) * 2`

Tree form:
```
        *
       / \
      +   2
     / \
    3   5
```
---

# ⚙️ How Evaluation Works

👉 We evaluate using **Postorder Traversal (Left → Right → Root)**

### Steps:
1. Traverse left subtree  
2. Traverse right subtree  
3. Apply operator  

---

## 🔢 Example Evaluation

Expression: `(3 + 5) * 2`

### Postorder traversal:


### Step-by-step:
- `3 + 5 = 8`
- `8 * 2 = 16`

👉 **Final Answer = 16**

---

# 🔁 Traversals & Expressions

| Traversal | Expression Type |
|----------|----------------|
| Inorder | Infix `(A + B)` |
| Preorder | Prefix `+ A B` |
| Postorder | Postfix `A B +` |

---

# 💻 Python Code for Evaluation

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate(root):
    # If leaf node (operand)
    if root.left is None and root.right is None:
        return int(root.value)

    # Evaluate left and right
    left_val = evaluate(root.left)
    right_val = evaluate(root.right)

    # Apply operator
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val / right_val

# Build tree manually for (3+5)*2
root = Node('*')
root.left = Node('+')
root.right = Node('2')
root.left.left = Node('3')
root.left.right = Node('5')

print(evaluate(root))  # Output: 16