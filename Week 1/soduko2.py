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

# Function to check if the grid is valid, including checking 3x3 boxes
def is_valid(grid):
    # Check if the grid is a 9x9 matrix
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        return False

    # Check for duplicates in rows, columns, and 3x3 boxes
    for i in range(9):
        row_numbers = [num for num in grid[i] if num != 0]
        if len(row_numbers) != len(set(row_numbers)):
            return False

        col_numbers = [grid[j][i] for j in range(9) if grid[j][i] != 0]
        if len(col_numbers) != len(set(col_numbers)):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box_numbers = []
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    if grid[r][c] != 0:
                        box_numbers.append(grid[r][c])
            if len(box_numbers) != len(set(box_numbers)):
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

# Main function to solve Sudoku
def solve_sudoku(grid):
    if not is_valid(grid):
        return "ERROR: Invalid grid"

    # Apply cross-hatching repeatedly until no more changes can be made
    while True:
        if not apply_cross_hatching(grid):
            break

    # Final check for contradictions or unsolved cells
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:  # If any cell is empty
                if not any(can_place(num, r, c, grid) for num in range(1, 10)):
                    return "ERROR: No solution possible"

    return grid

# Function to input a 9x9 Sudoku grid from the user
def input_sudoku_grid():
    print("Enter the Sudoku grid row by row. Use '.' for empty cells.")
    grid = []
    for i in range(9):
        while True:
            try:
                # Take row input
                row = input(f"Row {i + 1}: ").strip().split()
                # Validate row input: should contain exactly 9 entries of digits or '.'
                if len(row) != 9 or any(num not in "0123456789." for num in row):
                    raise ValueError
                # Convert '.' to 0 and append to the grid
                grid.append([0 if num == '.' else int(num) for num in row])
                break
            except ValueError:
                print("Invalid input. Please enter exactly 9 characters consisting of digits or '.' for empty cells.")
    return grid

# Input and solve Sudoku
sudoku_grid = input_sudoku_grid()
solution = solve_sudoku(sudoku_grid)
if isinstance(solution, str) and solution.startswith("ERROR"):
    print(solution)
else:
    print("Solved Sudoku:")
    print_grid(solution)
