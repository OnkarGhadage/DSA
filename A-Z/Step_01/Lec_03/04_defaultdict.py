from collections import defaultdict

graph = defaultdict(list)
edge = [(1, 0), (1, 2), (1, 3), (2, 4), (3, 8), (3, 9)]

for i,j in edge:
    graph[i].append(j)

print(graph)
print(dict(graph))