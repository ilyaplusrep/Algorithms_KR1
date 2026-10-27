from collections import deque

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['E','F'],
    'D': ['G'],
    'E': ['G','H'],
    'F': ['G'],
    'G': ['H'],
    'H': []
}

def topological_sort(graph):
    visited = set()
    result = []
    def dfs(v):
        visited.add(v)
        for nb in graph.get(v, []):
            if nb not in visited:
                dfs(nb)
        # вершина записывается после всех своих потомков
        result.append(v)
    for v in graph:
        if v not in visited:
            dfs(v)
    # разворот: теперь каждая вершина стоит раньше всех, кто от неё зависит
    return result[::-1]

print('Топологический порядок:', topological_sort(graph))

#-----------------------------------

def shortest_path(graph, start, end):
    parent = {start: None}  # откуда пришли в вершину; заодно служит visited
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == end:
            break
        for i in graph[current]:
            if i not in parent:
                parent[i] = current
                queue.append(i)

    if end not in parent:
        return None

    # идём от конца по предкам до старта и разворачиваем
    path = []
    v = end
    while v is not None:
        path.append(v)
        v = parent[v]
    return path[::-1]

path = shortest_path(graph, 'A', 'H')
print('Кратчайший путь A -> H:', ' -> '.join(path))
print('Длина (рёбер):', len(path) - 1)
