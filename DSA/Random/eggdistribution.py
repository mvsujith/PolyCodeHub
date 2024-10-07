import math
from collections import defaultdict
def dfs(node, visited, adj_list):  
    stack = [node]
    size = 0
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            size += 1
            for neighbor in adj_list[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return size
def connectedSum(graph_nodes, graph_from, graph_to):
    adj_list = defaultdict(list)
    for u, v in zip(graph_from, graph_to):
        adj_list[u].append(v)
        adj_list[v].append(u)
    visited = [False] * (graph_nodes + 1)  
    total_sum = 0
    for node in range(1, graph_nodes + 1):
        if not visited[node]: 
            component_size = dfs(node, visited, adj_list)
            total_sum += math.ceil(math.sqrt(component_size))
    return total_sum
graph_nodes = 4
graph_from = [1,1]
graph_to = [2,4]
print(connectedSum(graph_nodes, graph_from, graph_to)) 