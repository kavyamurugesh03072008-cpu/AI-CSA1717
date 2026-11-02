import heapq

def astar(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            print("Shortest path:", " -> ".join(path))
            print("Total cost:", cost)
            return

        if cost > best_cost.get(node, float('inf')):
            continue

        for neighbor, weight in graph[node].items():
            new_cost = cost + weight

            if new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]

                heapq.heappush(
                    queue,
                    (priority, new_cost, neighbor, path + [neighbor])
                )

    print("No path found")


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

astar(graph, heuristic, 'A', 'D')
