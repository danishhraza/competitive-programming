# The initial Sudoku grid
input_grid = [[0, 0, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 4, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 4, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 4, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

input_grid2 = [
    [0, 0, 0, 1, 0, 0, 0, 6, 0],  # Row 1: "...1...6."
    [1, 8, 0, 0, 0, 9, 0, 0, 0],  # Row 2: "18...9..."
    [0, 0, 7, 0, 6, 4, 2, 0, 0],  # Row 3: "..7.642.."
    [2, 0, 9, 0, 0, 6, 0, 5, 0],  # Row 4: "2.9..6.5."
    [0, 4, 3, 0, 0, 0, 7, 2, 0],  # Row 5: ".43...72."
    [0, 6, 0, 3, 0, 0, 9, 0, 1],  # Row 6: ".6.3..9.1"
    [0, 0, 2, 6, 5, 0, 1, 0, 0],  # Row 7: "..265.1.."
    [0, 0, 0, 2, 0, 0, 0, 9, 7],  # Row 8: "...2...97"
    [0, 5, 0, 0, 0, 3, 0, 0, 0]   # Row 9: ".5...3..."
]

input_grid3 = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 1: "1........"
    [0, 0, 1, 0, 0, 0, 0, 0, 0],  # Row 2: "..1......"
    [0, 0, 0, 0, 0, 0, 0, 1, 0],  # Row 3: ".......1."
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 4: "........."
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 5: "........."
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 6: "........."
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 7: "........."
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 8: "........."
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0, 0],   
]

input_grid4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 2],  # Row 1: "........2"
    [0, 0, 0, 0, 1, 0, 0, 0, 0],  # Row 2: "....1...."
    [1, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 3: "1........"
    [0, 0, 0, 0, 0, 0, 1, 0, 0],  # Row 4: "......1.."
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 5: "........."
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 6: "........."
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 7: "........."
    [0, 0, 0, 0, 0, 0, 0, 1, 0],  # Row 8: ".......1."
    [0, 0, 0, 0, 0, 0, 0, 0, 0]   # Row 9: "........."
]

# Function to print the Sudoku grid in a readable format
def print_grid(grid):
    for row in grid:
        print("".join(str(num) if num != 0 else '.' for num in row))

# Function to check if a number can be placed in a specific cell
def can_place(num, r, c, grid):
    # Check the row and column
    if num in grid[r] or num in [grid[i][c] for i in range(9)]:
        return False
    # Check the 3x3 box
    box_start_row, box_start_col = 3 * (r // 3), 3 * (c // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if grid[i][j] == num:
                return False
    return True

# Cross-hatching method
def apply_cross_hatching(grid):
    changes = False
    for num in range(1, 10):  # For each number from 1 to 9
        for box_row in range(0, 9, 3):  # Each 3x3 box (rows)
            for box_col in range(0, 9, 3):  # Each 3x3 box (columns)
                possible_positions = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if grid[r][c] == 0 and can_place(num, r, c, grid):
                            possible_positions.append((r, c))
                if len(possible_positions) == 1:
                    r, c = possible_positions[0]
                    grid[r][c] = num
                    changes = True
    return changes

# Function to check if the grid is valid
def is_valid(grid):
    for row in grid:
        if len(row) != 9:
            return False
    if len(grid) != 9:
        return False
    return True

# Main function to solve Sudoku
def solve_sudoku(grid):
    if not is_valid(grid):
        return "ERROR"
    # Apply cross-hatching repeatedly until no more changes can be made
    while True:
        if not apply_cross_hatching(grid):
            break
    # Final check for contradictions
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:  # If any cell is empty
                if not any(can_place(num, r, c, grid) for num in range(1, 10)):
                    return "ERROR"
    return grid

# Solve the Sudoku and print the result
solution = solve_sudoku(input_grid4)
if solution == "ERROR":
    print("ERROR")
else:
    print_grid(solution)
