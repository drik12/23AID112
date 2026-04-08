V = 4

# Initialize matrix with 0
graph = [[0 for _ in range(V)] for _ in range(V)]

def add_edge(u, v):
    graph[u][v] = 1
    graph[v][u] = 1  # remove for directed graph

# Add edges
add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 2)
add_edge(2, 3)

# Print matrix
for row in graph:
    print(row)