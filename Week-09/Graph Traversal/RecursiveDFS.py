# Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

def dfs_recursive(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Driver Code
if __name__ == "__main__":
    visited = set()
    start_node = 'A'

    print("DFS Traversal (Recursive):", end=" ")
    dfs_recursive(graph, start_node, visited)