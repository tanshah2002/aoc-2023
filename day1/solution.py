
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()


# Part 1
calibration_value_sum = 0

for line in lines:
    line_nums = [int(char) for char in line if char.isnumeric()]
    if line_nums:
        calibration_value_sum += int(f'{line_nums[0]}{line_nums[-1]}')

print(f'Part 1 Result: {calibration_value_sum}')

# Part 2
calibration_value_sum_accurate = 0
number_word_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def find_all_starting_positions(line, target):
    starting_positions = []

    for i in range(len(line)):
        sub_str = line[i : i + len(target)]
        if sub_str == target:
            starting_positions.append((target, i))


    return starting_positions

for line in lines:  
    number_index_pairs = []

    for number_word, number_char in number_word_map.items():
        number_index_pairs += find_all_starting_positions(line, number_word)
        number_index_pairs += find_all_starting_positions(line, number_char)

    if number_index_pairs:
        min_pair_number = min(number_index_pairs, key=lambda pair: pair[1])[0]
        max_pair_number = max(number_index_pairs, key=lambda pair: pair[1])[0]
        first_digit = number_word_map[min_pair_number] if min_pair_number in number_word_map else min_pair_number
        last_digit = number_word_map[max_pair_number] if max_pair_number in number_word_map else max_pair_number
        final_line_numbr = int(f'{first_digit}{last_digit}')

        calibration_value_sum_accurate += final_line_numbr


print(f'Part 2 Result: {calibration_value_sum_accurate}')