from collections import deque

def solve_puzzle(start, goal):
    queue = deque([(start, [])])
    visited = {tuple(start)}

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        zero = state.index(0)
        x, y = divmod(zero, 3)

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_pos = nx * 3 + ny
                new_state = state[:]
                new_state[zero], new_state[new_pos] = (
                    new_state[new_pos], new_state[zero]
                )

                key = tuple(new_state)

                if key not in visited:
                    visited.add(key)
                    queue.append((new_state, path + [state]))

    return None


start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution = solve_puzzle(start, goal)

if solution:
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()
else:
    print("No solution exists")
