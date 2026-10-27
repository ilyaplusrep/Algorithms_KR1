graph = {
    1: [2,3],
    2: [1,4,5],
    3: [1,6,7],
    4: [2,8],
    5: [2,8],
    6: [3,9],
    7: [3,9],
    8: [4,5,10],
    9: [6,7,10],
    10: [8,9]
}

def dfs_stack(graph, start):
    visited = []
    stack = [start]

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)
        print(f'{current} - is visited')
        #reversed чтобы соседи обходились по возрастанию, как в рекурсивном DFS
        for i in reversed(graph[current]):
            if i not in visited:
                stack.append(i)
    return visited

result1 = dfs_stack(graph, 1)
print(result1)

#------------ BFS
print('--------------------------')
from collections import deque

def bfs(graph, start):
    visited = {start}
    order = []
    queue = deque([start])

    while queue:
        current = queue.popleft()
        order.append(current)

        for i in graph[current]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
            
    return order

print(bfs(graph,1))
