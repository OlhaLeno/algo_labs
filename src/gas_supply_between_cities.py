def dfs(graph, start, visited):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return


def gas_supply(cities, storages, pipes):
    graph = {}
    for city in cities + storages:
        graph[city] = []

    for pipe in pipes:
        source, end = pipe
        graph[source].append(end)

    unreachable_cities = {}
    for storage in storages:
        visited = set()
        dfs(graph, storage, visited)
        unreachable = set(cities) - visited
        if unreachable:
            unreachable_cities[storage] = list(unreachable)

    return unreachable_cities


cities = ['Lviv', 'Striy', 'Dolina', 'Kyiv', 'Mykolaiv']
storages = ['storage_1', 'storage_2']
pipes = [['Lviv', 'Striy'], ['storage_1', 'Lviv'], ['Lviv', 'Dolina'], ['Lviv', 'Kyiv']]
print(gas_supply(cities, storages, pipes))
