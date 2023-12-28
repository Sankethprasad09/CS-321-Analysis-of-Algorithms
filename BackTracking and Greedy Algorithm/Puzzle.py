def reachTreasure(puzzle):
    n = len(puzzle)

    def backtrack(row, col):
        if row < 0 or row >= n or col < 0 or col >= n or puzzle[row][col] != 1:
            return False

        if row == n - 1 and col == n - 1:
            return True

        puzzle[row][col] = -1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            if backtrack(newRow, newCol):
                return True

        puzzle[row][col] = 1
        return False

    return backtrack(0, 0)

# User input
n = int(input("Enter the size of the matrix (nxn): "))
puzzle = []
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1} of the matrix (separated by spaces): ").split()))
    puzzle.append(row)

# Call the function and display the result
result = reachTreasure(puzzle)
print(f"Can you reach the treasure? {'Yes' if result else 'No'}")
