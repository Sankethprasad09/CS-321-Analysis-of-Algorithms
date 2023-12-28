import copy  # We need copy library for duplicating lists

# This function finds the shortest path from Source to Destination on the Board
def solve_puzzle(Board, Source, Destination):
    # Store the number of rows and columns in the Board
    row = len(Board)
    col = len(Board[0])
    
    # Initialize an empty queue for breadth-first search (BFS)
    queue = []
    
    # Enqueue the source with its path and direction string
    queue.append([Source, [Source], ""])
    
    # List to track the positions we have already visited
    traversed = []
    
    # Array for representing the four possible moves (left, right, up, down)
    dim = [[0, -1, 'L'], [0, 1, 'R'], [-1, 0, 'U'], [1, 0, 'D']]
    
    # Continue till there are elements in the queue
    while len(queue) > 0:
        # Dequeue the front element
        grid = queue.pop(0)
        (i, j) = grid[0]
        path = grid[1]
        dir = grid[2]
        
        # Add current position to traversed list
        traversed.append((i, j))
        
        # If we have reached the destination, return the path and direction string
        if ((i, j) == Destination):
            return (path, dir)
        
        # Check each possible move
        for ki, kj, d in dim:
            # Calculate new position
            ii = ki + i
            jj = kj + j
            
            # If new position is valid, not visited before and not an obstacle, enqueue it
            if ii < 0 or ii >= row or jj < 0 or jj >= col or (ii, jj) in traversed or Board[ii][jj] == '#':
                continue
                
            newPath = copy.copy(path)
            newPath.append((ii, jj))
            
            # Enqueue new position with updated path and direction string
            queue.append([(ii, jj), newPath, dir + d])
            
    # If no valid path is found, return None
    return None
# The puzzle board
puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]

# Testing the function with different source and destination points
print(solve_puzzle(puzzle, (0, 2), (2, 2)))  # Expected output: ([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR')
print()
print(solve_puzzle(puzzle, (0, 0), (4, 4)))  # Expected output: ([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], 'RRRRDDDD')
print()
print(solve_puzzle(puzzle, (0, 0), (4, 0)))  # Expected output: None
print()
