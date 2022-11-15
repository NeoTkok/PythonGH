vertices = list(map(int, input().split()))
graph = {}
for i in range(len(vertices)):
    graph[vertices[i]] = []

n_edges = int(input())
for i in range(n_edges):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

v_search = list(map(int, input().split()))
v_find = set()
for v in v_search:
    v_find.add(v)
    for v_f in graph[v]:
        v_find.add(v_f)
v_find = list(v_find)
v_find.sort()
print(*v_find)