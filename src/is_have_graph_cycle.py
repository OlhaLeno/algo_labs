from collections import deque


def have_cycle(graph):
    for vertex in graph:
        if bfs(graph, vertex):
                return True
    return False


def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
        return False


def read_graph(file_name):
    graph = {}
    with open(file_name, "r") as file:
        for line in file:
            graph = list(map(int, line.strip().split()))
            vertex = graph[0]
            neighbors = graph[1:]
            graph[vertex] = neighbors
        file.close()
    return graph


def write_result(file_name, have_cycle):
    with open(file_name, "w") as file:
        file.write(str(have_cycle))
    file.close()
    return file


if __name__ == "main":
    graph = read_graph("input.txt")
    result = have_cycle(graph)
    write_result(result, "output.txt")
