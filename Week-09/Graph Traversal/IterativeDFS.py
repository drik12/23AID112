# Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    print("DFS Traversal (Iterative):", end=" ")

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Reverse ensures correct order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Driver Code
if __name__ == "__main__":
    start_node = 'A'
    dfs_iterative(graph, start_node)