# Add Edge in undirected and unweighted graph using adjacency List method
def add_node(v):
    if v in graph:
        print(v,"is present in graph.")
    else:
        graph[v] = []

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in graph.")
    elif v2 not in graph:
        print(v2,"is not present in graph.")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

graph = {}
add_node("A")
add_node("B")
add_node("C")

add_edge("A","B")
add_edge("B","C")
add_edge("C","A")
print(graph)