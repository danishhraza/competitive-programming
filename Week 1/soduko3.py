def cross_hatching_solver(lines):
    grid = []
    for r in range(9):
        row = []
        for c in range(9):
            ch = lines[r][c]
            if ch == '.':
                row.append(0)
            else:
                val = int(ch)
                if not (1 <= val <= 9):
                    return "ERROR"
                row.append(val)
        grid.append(row)

    row_used = [set() for _ in range(9)]
    col_used = [set() for _ in range(9)]
    box_used = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = grid[r][c]
            if val != 0:
                box_index = (r // 3) * 3 + (c // 3)
                if (val in row_used[r] or 
                    val in col_used[c] or 
                    val in box_used[box_index]):
                    return "ERROR"
                row_used[r].add(val)
                col_used[c].add(val)
                box_used[box_index].add(val)

    while True:
        changed = False

        for digit in range(1, 10):
            for box_index in range(9):
                if digit in box_used[box_index]:
                    continue

                r_start = (box_index // 3) * 3
                c_start = (box_index % 3) * 3

                possible_positions = []
                for rr in range(r_start, r_start + 3):
                    for cc in range(c_start, c_start + 3):
                        if grid[rr][cc] == 0:
                            if (digit not in row_used[rr] and
                                digit not in col_used[cc]):
                                possible_positions.append((rr, cc))

                if len(possible_positions) == 0:
                    return "ERROR"

                if len(possible_positions) == 1:
                    (rpos, cpos) = possible_positions[0]
                    grid[rpos][cpos] = digit
                    row_used[rpos].add(digit)
                    col_used[cpos].add(digit)
                    box_used[box_index].add(digit)
                    changed = True

        if not changed:
            break

    result = []
    for r in range(9):
        row_str = ""
        for c in range(9):
            val = grid[r][c]
            row_str += str(val) if val != 0 else '.'
        result.append(row_str)

    return result


if __name__ == "__main__":
    import sys
    lines = [sys.stdin.readline().rstrip('\n') for _ in range(9)]
    answer = cross_hatching_solver(lines)
    if answer == "ERROR":
        print("ERROR")
    else:
        for row in answer:
            print(row)
