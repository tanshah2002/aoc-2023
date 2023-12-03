from collections import defaultdict

with open('input.txt', 'r') as file:
    engine_matrix = [list(line) for line in file.read().splitlines()]

in_bounds = lambda y, x: y >= 0 and y < len(engine_matrix) and x >= 0 and x < len(engine_matrix[0])

def get_neighboring_positions(position):
    y, x = position
    pos_changes = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    neighboring_positions = []
    for dy, dx in pos_changes:
        neighbor_y = y + dy
        neighbor_x = x + dx

        if in_bounds(neighbor_y, neighbor_x):
            neighboring_positions.append((neighbor_y, neighbor_x))

    return neighboring_positions

def has_symbol_neighbor(neighboring_positions):
    symbol_char_positions = []
    symbol_flag = False

    for neighbor_pos in neighboring_positions:
        y, x = neighbor_pos
        if not engine_matrix[y][x].isnumeric() and engine_matrix[y][x] != '.':
            symbol_flag = True
            symbol_char_positions.append((neighbor_pos, engine_matrix[y][x]))

    return symbol_flag, symbol_char_positions

symbol_part_nums = defaultdict(list)

# Part 1
part_num_sum = 0
visited_positions = set()

for row_index, row in enumerate(engine_matrix):
    for col_index, char in enumerate(row):
        neighboring_positions = get_neighboring_positions((row_index, col_index))
        symbol_flag, symbol_char_positions = has_symbol_neighbor(neighboring_positions)
    
        if (row_index, col_index) not in visited_positions and char.isnumeric() and symbol_flag:
            # compute the current number
            cur_number = ""
            l_index = col_index

            # traverse left in the current row
            while l_index >= 0 and engine_matrix[row_index][l_index].isnumeric():
                cur_number = engine_matrix[row_index][l_index] + cur_number
                visited_positions.add((row_index, l_index))

                l_index -= 1

            # traverse right in the current row
            r_index = col_index + 1

            while r_index < len(engine_matrix[0]) and engine_matrix[row_index][r_index].isnumeric():
                cur_number += engine_matrix[row_index][r_index]
                visited_positions.add((row_index, r_index))

                r_index += 1

            part_num = int(cur_number)
            part_num_sum += part_num

            for symbol_char_position in symbol_char_positions:
                symbol_part_nums[symbol_char_position].append(part_num)

print(f"Part 1: {part_num_sum}")

# Part 2
gear_ratio_sum = 0

for symbol_pos_data, part_nums in symbol_part_nums.items(): 
    symbol_pos, symbol = symbol_pos_data
    if symbol == '*' and len(part_nums) == 2:
        gear_ratio_sum += part_nums[0] * part_nums[-1]

print(f"Part 2: {gear_ratio_sum}")    