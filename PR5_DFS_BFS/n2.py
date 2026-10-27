graph = {
    'A': ['B','C'],
    'B': ['A','C'],
    'C': ['A','B','D'],
    'D': ['C'],

    'E': ['F'],
    'F': ['E','G'],
    'G': ['F'],

    'H': [],

    'I': ['J','L'],
    'J': ['I','K'],
    'K': ['J','L'],
    'L': ['I','K']
}

globalVisited = []

def dfs_stack(graph, start):
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)
        #print(f'{current} - is visited')
        #reversed чтобы соседи обходились по возрастанию, как в рекурсивном DFS
        for i in reversed(graph[current]):
            if i not in visited:
                stack.append(i)
    globalVisited.extend(visited)
    return visited

components=[]
for dot in graph:
    if dot not in globalVisited:
        result = dfs_stack(graph, dot)
        components.append(result)
print([set(comp) for comp in components])

#-----------------------------------

from collections import deque

def bfs(graph, start):
    colorVisited = {start: 0}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if i not in colorVisited:
                if colorVisited[current]==0:
                    colorVisited[i]=1
                else:
                    colorVisited[i]=0
                queue.append(i)
            else:
                if colorVisited[i]==colorVisited[current]:
                    return False, [i, current]
    return True, colorVisited

for comp in components:
    ok,data = bfs(graph, comp[0])
    print(comp)
    if ok:
        print(f'Двудольный, раскраска: {data}')
    else:
        print(f'Недвудольный, совпадение цветов в вершинах: {data}')