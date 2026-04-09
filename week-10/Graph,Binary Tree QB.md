# 🌐 Graph-Based Questions (Verbose)

---

## Question 1: Social Network Analysis

### Scenario
A social media platform stores millions of users and their friendships. Each user can be connected to many other users. The system should efficiently manage relationships and allow operations like finding mutual friends, suggesting new connections, and displaying all friends of a user.

### System Behavior
- Users are represented as nodes (vertices)
- Friendships are represented as edges
- Connections are mutual (undirected graph)

### Tasks

#### 1. Identify Data Structure
Identify the most suitable graph representation (adjacency list or adjacency matrix) and justify your choice based on space efficiency.

#### 2. Explanation
Explain how an adjacency list can represent user connections efficiently.

#### 3. Pseudocode
Write pseudocode for:
- Adding a user
- Adding a friendship
- Displaying all friends of a given user

#### 4. Time Complexity
Analyze the time complexity for:
- Adding a user
- Adding an edge
- Searching for friends

### Implementation Task
Write a Python program using adjacency list with functions:
- `add_user(user)`
- `add_friend(u, v)`
- `display_friends(user)`

---

## Question 2: Shortest Path in Navigation System

### Scenario
A navigation system must find the shortest route between two cities. Each road has a distance, and the system must always choose the minimum distance path.

### System Behavior
- Cities are nodes
- Roads are weighted edges
- Graph is weighted and may be directed or undirected

### Tasks

#### 1. Identify Algorithm
Choose the most suitable algorithm (Dijkstra’s Algorithm) and justify why it is preferred over BFS.

#### 2. Explanation
Explain how priority queues help in selecting the next shortest node.

#### 3. Pseudocode
Write pseudocode for Dijkstra’s Algorithm.

#### 4. Time Complexity
Analyze time complexity in terms of:
- Number of vertices (V)
- Number of edges (E)

### Implementation Task
Write a Python program with:
- `add_edge(u, v, weight)`
- `dijkstra(source)`

---

## Question 3: Course Scheduling System

### Scenario
A university system manages course prerequisites. Some courses must be completed before others. The system must determine a valid order to complete all courses.

### System Behavior
- Courses are nodes
- Prerequisites are directed edges
- No cycles allowed (Directed Acyclic Graph)

### Tasks

#### 1. Identify Data Structure
Explain why a Directed Acyclic Graph (DAG) is suitable.

#### 2. Explanation
Explain Topological Sorting and its importance.

#### 3. Pseudocode
Write pseudocode for Topological Sort using DFS or Kahn’s Algorithm.

#### 4. Time Complexity
Analyze time complexity of topological sorting.

### Implementation Task
Write a Python program with:
- `add_course(course)`
- `add_prerequisite(A, B)`
- `topological_sort()`

---

# 🌳 Binary Tree-Based Questions (Verbose)

---

## Question 4: File System Representation

### Scenario
An operating system organizes files and directories in a hierarchical structure. Each directory can contain files or subdirectories.

### System Behavior
- Root directory at top
- Each node has parent-child relationship
- Structure resembles a tree

### Tasks

#### 1. Identify Data Structure
Explain why a tree is the most suitable structure.

#### 2. Explanation
Describe parent, child, leaf, and root nodes.

#### 3. Pseudocode
Write pseudocode for:
- Inserting a node
- Traversing the tree (DFS)

#### 4. Time Complexity
Analyze time complexity of traversal.

### Implementation Task
Write a Python program with:
- `insert(node)`
- `display_tree()`

---

## Question 5: Binary Search Tree for Fast Lookup

### Scenario
A system stores student roll numbers and allows quick searching, insertion, and deletion.

### System Behavior
- Left subtree contains smaller values
- Right subtree contains larger values

### Tasks

#### 1. Identify Data Structure
Explain why Binary Search Tree is efficient for searching.

#### 2. Explanation
Explain insertion and search operations.

#### 3. Pseudocode
Write pseudocode for:
- Insert
- Search

#### 4. Time Complexity
Analyze:
- Best case
- Worst case

### Implementation Task
Write a Python program with:
- `insert(value)`
- `search(value)`
- `inorder()`

---

## Question 6: Expression Tree Evaluation

### Scenario
A compiler evaluates arithmetic expressions using a tree structure where operands are leaves and operators are internal nodes.

Example:
(8 + 2) * 5

### System Behavior
- Binary tree representation
- Postfix expressions used for construction

### Tasks

#### 1. Identify Data Structure
Explain why binary trees are suitable for expression evaluation.

#### 2. Explanation
Describe how postfix expressions are converted into trees.

#### 3. Pseudocode
Write pseudocode to:
- Build expression tree
- Evaluate expression

#### 4. Time Complexity
Analyze time complexity of evaluation.

### Implementation Task
Write a Python program with:
- `build_tree(expression)`
- `evaluate()`

---