# Number of vertices
V = 4

# Create adjacency list
graph = [[] for _ in range(V)]

# Add edges
def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)  # remove this line for directed graph

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 2)
add_edge(2, 3)

# Print adjacency list
for i in range(V):
    print(f"{i} -> {graph[i]}")