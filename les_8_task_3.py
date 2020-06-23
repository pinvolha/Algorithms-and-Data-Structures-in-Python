# Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


def graph_gen(n):
    i = 0
    g = [[0] * (n - 1) for _ in range(n)]
    while i < n:
        g[i] = [_ for _ in range(n)]
        g[i].pop(i)
        set(g[i])
        i += 1
    return g


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return print(visited)


v = int(input("Enter number of vertex:"))
graph = graph_gen(v)
print(*graph, sep='\n')
print("*" * 10)
dfs(graph, 3)
