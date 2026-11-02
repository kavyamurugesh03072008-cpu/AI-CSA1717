from collections import deque

def water_jug():
    capacity = (4, 3)
    start = (0, 0)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == 2 or b == 2:
            for state in path + [(a, b)]:
                print(state)
            return

        amount = [
            (4, b), (a, 3), (0, b), (a, 0),
            (a - min(a, 3 - b), b + min(a, 3 - b)),
            (a + min(b, 4 - a), b - min(b, 4 - a))
        ]

        for state in amount:
            x, y = state

            if 0 <= x <= 4 and 0 <= y <= 3:
                if state not in visited:
                    visited.add(state)
                    queue.append((state, path + [(a, b)]))

water_jug()
