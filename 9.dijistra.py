#djikstra code
import sys
def dijkstra(graph, start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    print(distances)
    visited = set()

    while len(visited) != len(graph):
        min_distance = sys.maxsize
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        visited.add(min_node)
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4},
    'C': {'B': 1, 'D': 7},
    'D': {'E': 3},
    'E': {}
}
start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node)
for node, distance in shortest_distances.items():
    print(node, ":", distance)