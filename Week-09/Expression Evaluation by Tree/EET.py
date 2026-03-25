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