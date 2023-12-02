
with open('input.txt', 'r') as file:
    games = file.read().splitlines()


# Part 1
# only 12 red cubes, 13 green cubes, and 14 blue cubes for the ids

config_p1 = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def is_possible_with_config(cubes_data, config):
    bag_draws = [draw.strip() for draw in cubes_data.split(';')]
    for bag_draw in bag_draws:
        cube_counts = [pair.strip() for pair in bag_draw.split(',')]
        for cube_count in cube_counts:
            count, color = cube_count.split(' ')
            if int(count) > config[color]:
                return False

    return True


p1_id_sum = 0
for game_information in games:
    game_id_data, cubes_data = game_information.split(':')
    game_id = int(game_id_data.replace('Game ', ''))


    if is_possible_with_config(cubes_data, config_p1):
        p1_id_sum += game_id

print(f'Part 1: {p1_id_sum}')

# Part 2

def min_color_powerset_of_game(cubes_data):
    max_color_map = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    bag_draws = [draw.strip() for draw in cubes_data.split(';')]

    for bag_draw in bag_draws:
        cube_counts = [pair.strip() for pair in bag_draw.split(',')]
        for cube_count in cube_counts:
            count, color = cube_count.split(' ')
            max_color_map[color] = max(max_color_map[color], int(count))        

    return max_color_map['blue'] * max_color_map['red'] * max_color_map['green']    

min_cube_powerset_sum = 0

for game_information in games:
    _, cubes_data = game_information.split(':')
    min_cube_powerset_sum += min_color_powerset_of_game(cubes_data)

print(f'Part 2: {min_cube_powerset_sum}')

