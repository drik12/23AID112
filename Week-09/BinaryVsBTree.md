# 🌳 Difference Between Binary Tree and B-Tree

## 🔹 Binary Tree
- Each node has **at most 2 children** (left and right)
- Each node stores **only one key**
- Structure may be **unbalanced**
- Height can become large (inefficient in worst case)
- Simpler to implement
- Used in:
  - Expression trees
  - Binary Search Trees (BST)

---

## 🔹 B-Tree
- Each node can have **multiple children** (more than 2)
- Each node stores **multiple keys**
- Always **self-balanced**
- Height is small (efficient for large data)
- More complex structure
- Used in:
  - Databases
  - File systems

---

## ⚔️ Key Differences

| Feature | Binary Tree | B-Tree |
|--------|------------|--------|
| Children per node | Max 2 | Many (depends on order) |
| Keys per node | 1 | Multiple |
| Balance | Not guaranteed | Always balanced |
| Height | Can be large | Small |
| Search efficiency | Slower if unbalanced | Faster |
| Use case | General purpose | Databases, indexing |

---

## 🧠 One-line Answer

**A Binary Tree allows at most two children per node and may be unbalanced, whereas a B-Tree is a balanced multi-way tree where each node contains multiple keys and children, making it efficient for database indexing.**