
with open('input.txt', 'r') as file:
    race_times_allowed_raw, race_record_distances_raw = file.read().splitlines()
    race_times_allowed =[int(time) for time in race_times_allowed_raw.replace('Time:', '').split(' ') if time.strip()]
    race_record_distances = [int(distance) for distance in race_record_distances_raw.replace('Distance:', '').split(' ') if distance.strip()]

# Part 1
num_way_to_beat_record = 1

for race_time, race_distance in zip(race_times_allowed, race_record_distances):
    possible_ways_to_win_for_race = 0

    for time_holding_button in range(race_time + 1):
        remaining_time = race_time - time_holding_button
        distance_travelled = remaining_time * time_holding_button

        if distance_travelled > race_distance:
            possible_ways_to_win_for_race += 1

    num_way_to_beat_record *= possible_ways_to_win_for_race

print(f'Part 1: {num_way_to_beat_record}')

# Part 2
actual_race_time = int(''.join(str(time) for time in race_times_allowed))
actual_record_distance = int(''.join(str(distance) for distance in race_record_distances))

total_ways_longer_race = 0

for time_holding_button in range(actual_race_time + 1):
        remaining_time = actual_race_time - time_holding_button
        distance_travelled = remaining_time * time_holding_button

        if distance_travelled > actual_record_distance:
            total_ways_longer_race += 1

print(f'Part 2: {total_ways_longer_race}')