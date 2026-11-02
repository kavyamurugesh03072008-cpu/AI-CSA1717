from itertools import permutations

def tsp(graph, start):
    cities = list(graph.keys())
    others = [city for city in cities if city != start]

    min_cost = float('inf')
    best_path = None

    for route in permutations(others):
        path = [start] + list(route) + [start]
        cost = 0

        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            best_path = path

    print("Shortest path:", " -> ".join(best_path))
    print("Minimum cost:", min_cost)


graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

tsp(graph, 'A')
