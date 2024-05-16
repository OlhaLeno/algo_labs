from typing import List, Tuple
from collections import defaultdict

SOURCE = "SOURCE"
SINK = "SINK"


def read_file(file_name: str) -> Tuple[List[str], List[str], List[List[str]]]:
    """
     Reads the input file containing information about farms, stores and road capacities.

     Parameters:
     - file_name (str): The name of the input file.

     Returns:
     Tuple[List[str], List[str], List[List[str]]]: A tuple containing lists of farms, stores and roads.
     """
    with open(f"../resources/{file_name}", "r") as file:
        lines = file.readlines()
        farms = lines[0].strip().split()
        stores = lines[1].strip().split()
        roads = [line.strip().split() for line in lines[2:]]
    return farms, stores, roads


def dfs(graph, visited, start: str = SOURCE, end: str = SINK) -> List[List[str]]:
    """
      Uses a depth-first search (DFS) algorithm on a graph to find paths from the start to the end node.

      Parameters:
      - graph (dict): The graph represented as a dictionary.
      - visited (set): A set containing visited nodes.
      - start (str): The starting node for the search (default is SOURCE).
      - end (str): The ending node for the search (default is SINK).

      Returns:
      List[List[str]]: A list of paths from start to end.
      """
    stack = [(start, [start])]
    paths = []
    if visited is None:
        visited = set()

    while stack:
        vertex, path = stack.pop()
        if vertex not in visited:
            visited.add(vertex)

            if vertex == end:
                paths.append(path)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return paths


def ford_fulkerson(graph, source, sink) -> int:
    """
      Finds the maximum flow in a flow network using the Ford-Fulkerson algorithm.

      Parameters:
      - graph (dict): The flow network graph represented as a dictionary.
      - source: The source node in the flow network.
      - sink: The sink node in the flow network.

      Returns:
      int: The maximum flow in the flow network.
      """
    parent = [-1] * len(graph)
    max_flow = 0

    while dfs(graph, [], source, sink):
        path_flow = float("Inf")
        current_node = sink
        while current_node != source:
            path_flow = min(path_flow, graph[parent[current_node]][current_node])
            current_node = parent[current_node]
        max_flow += path_flow

        node = sink
        while node != source:
            prev_node = parent[node]
            graph[prev_node][node] -= path_flow
            graph[node][prev_node] += path_flow
            node = parent[node]

    return max_flow


def create_graph(farms, stores, roads) -> dict:
    """
    Creates a flow network graph based on input data.

    Parameters:
    - farms (List[str]): List of farms.
    - stores (List[str]): List of stores.
    - roads (List[List[str]]): List of road connections between farms, stores and their capacities.

    Returns:
    dict: The flow network graph represented as a dictionary.
    """
    graph = defaultdict(dict)
    for road in roads:
        start, end, capacity = road
        graph[start][end] = int(capacity)
    for farm in farms:
        if farm not in graph:
            graph[farm] = {}
        graph[SOURCE][farm] = float('inf')
    for store in stores:
        if store not in graph:
            graph[store] = {}
        graph[store][SINK] = float('inf')
    return dict(graph)


def find_path(graph, start: str = SOURCE, end: str = SINK) -> List[List[str]]:
    """
    Finds paths from the start to the end node in the graph using depth-first search.

    Parameters:
    - graph (dict): The graph represented as a dictionary.
    - start (str): The starting node for the search (default is SOURCE).
    - end (str): The ending node for the search (default is SINK).

    Returns:
    List[List[str]]: A list of paths from start to end.
    """
    stack = [(start, [start])]
    paths = []
    while stack:
        vertex, path = stack.pop()
        neighbours = graph[vertex].keys()
        for neighbour in neighbours:
            if neighbour not in path:
                new_path = path + [neighbour]
                if neighbour == end:
                    paths.append(new_path)
                else:
                    stack.append((neighbour, new_path))
    return paths


def max_flow(graph) -> int:
    """
    Calculates the maximum flow in the flow network graph using the Ford-Fulkerson algorithm.

    Parameters:
    - graph (dict): The flow network graph represented as a dictionary.

    Returns:
    int: The maximum flow in the flow network.
    """
    maximum_flow = 0
    paths = find_path(graph)
    for path in paths:
        min_capacity = float('inf')
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            if graph[start][end] < min_capacity:
                min_capacity = graph[start][end]

        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            graph[start][end] -= min_capacity

            if graph[start][end] == 0:
                graph[start][end] = float('inf')

        maximum_flow += min_capacity

    return maximum_flow


def find_max_amount(file_name) -> int:
    """
      Finds the maximum amount of flow that can be sent from the source to the sink.

      Parameters:
      - file_name (str): The name of the input file containing farm, store and road information.

      Returns:
      int: The maximum amount of flow that can be sent from the source to the sink.
      """

    farms, stores, roads = read_file(file_name)
    graph = create_graph(farms, stores, roads)
    return max_flow(graph)
