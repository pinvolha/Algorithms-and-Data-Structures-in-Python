# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям
# (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

n = int(input("Enter vertex number: "))
graph = [[0] * n for _ in range(n)]
sum_edge = 0

for r in range(n):
    for c in range(n):
        if r != c:
            graph[r - 1][c - 1] = graph[c - 1][r - 1] = 1

print(*graph, sep='\n')

for r in range(n):
    for c in range(n):
        if graph[r][c] == 0:
            break
        else:
            sum_edge += graph[r][c]

print('Total unique edges = ', sum_edge)
