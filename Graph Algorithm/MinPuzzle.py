import heapq

def minEffort(puzzle):
    m, n = len(puzzle), len(puzzle[0])
    # Initialize effort matrix with maximum integer values
    effort = [[float('inf')] * n for _ in range(m)]
    effort[0][0] = 0

    # Define possible moves: up, down, left, right
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Initialize priority queue with the starting cell
    queue = [(0, 0, 0)]  # (effort, row, column)

    while queue:
        curr_effort, x, y = heapq.heappop(queue)
        if x == m-1 and y == n-1:
            return curr_effort
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                next_effort = max(curr_effort, abs(puzzle[nx][ny] - puzzle[x][y]))
                if next_effort < effort[nx][ny]:
                    effort[nx][ny] = next_effort
                    heapq.heappush(queue, (next_effort, nx, ny))

puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(minEffort(puzzle))  # Outputs: 1

