import sys

with open('input.txt', 'r') as file:
    farming_raw_information = file.read().splitlines()

def get_farming_data(farming_raw_information):
    farming_data = {
        'initial_seeds': [],
        'seed-to-soil map:': [],
        'soil-to-fertilizer map:': [],
        'fertilizer-to-water map:': [],
        'water-to-light map:': [],
        'light-to-temperature map:': [],
        'temperature-to-humidity map:': [],
        'humidity-to-location map:': []
    }

    cur_farming_group = None

    for line in farming_raw_information:
        if not line: continue

        elif line.startswith('seeds:'):
            seeds = [int(seed) for seed in line.replace('seeds:', '').split(' ') if seed.strip()]
            for seed in seeds:
                farming_data['initial_seeds'].append(seed)

        elif line.endswith('map:'):
            cur_farming_group = line
        
        else:
            farming_numbers = [int(number) for number in line.split(' ')]
            farming_data[cur_farming_group].append(farming_numbers)

    return farming_data

def get_lowest_location_number(farming_data):
    lowest_location_number = sys.maxsize
    all_seeds = farming_data['initial_seeds']

    for seed in all_seeds:
        lowest_location_number = min(lowest_location_number, get_location_number_from_seed(seed, farming_data))

    return lowest_location_number

def get_location_number_from_seed(seed, farming_data):
    cur_num = seed 
    
    for group, data_ranges in farming_data.items():
        if group != 'initial_seeds':
            for dest, source, num_range in data_ranges:
                min_source, max_source = source, (source + num_range) - 1
                diff = dest - source
            
                if cur_num in range(min_source, max_source + 1):
                    cur_num += diff
                    break
        
    return cur_num

def get_seed_number_from_location(location, farming_data):
    cur_num = location 

    for group, data_ranges in reversed(farming_data.items()):
        if group != 'initial_seeds':
            for source, dest, num_range in data_ranges:
                min_source, max_source = source, (source + num_range) - 1
                diff = dest - source
            
                if cur_num in range(min_source, max_source + 1):
                    cur_num += diff
                    break
        
    return cur_num

def get_seed_intervals(seeds):
    seed_intervals = []

    for i in range(0, len(seeds), 2):
        seed_range = seeds[i + 1]
        seed_range_start = seeds[i]
        seed_range_end = (seed_range_start + seed_range) - 1

        seed_intervals.append(range(seed_range_start, seed_range_end + 1))

    return seed_intervals

# Part 1

farming_data = get_farming_data(farming_raw_information)
lowest_location_number = get_lowest_location_number(farming_data)

print(f'Part 1: {lowest_location_number}')

# Part 2

current_seeds = farming_data['initial_seeds']
seed_intervals = get_seed_intervals(current_seeds)
updated_lowest_location_number = None
found_seed_interval = False
cur_location = 1

while not found_seed_interval:
    seed_number = get_seed_number_from_location(cur_location, farming_data)

    for seed_interval in seed_intervals:
        if seed_number in seed_interval:
            found_seed_interval = True
            updated_lowest_location_number = cur_location
            break 

    cur_location += 1

print(f'Part 2: {updated_lowest_location_number}')