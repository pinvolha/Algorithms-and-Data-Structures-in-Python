# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

from collections import deque

graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

# См. начиная со строки 45
def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    shortcut = {}
    for i in range(length):
        if cost[i] == 0:
            shortcut[i] = i
        elif cost[i] == float("inf"):
            shortcut[i] = "нет пути"
        else:
            n = i
            temp = deque()
            temp.appendleft(i)
            while True:
                temp.appendleft(parent[n])
                n = parent[n]
                if parent[n] == -1:
                    break
            shortcut[i] = list(temp)

    return shortcut


start = int(input("Введите начальную вершину: "))
paths = dijkstra(graph, start)
for key, value in paths.items():
    print("Кратчайший путь к вершине {}: {}".format(key, value))
