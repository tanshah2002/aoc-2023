
with open('input.txt', 'r') as file:
    histories = file.read().splitlines()    

def generate_pyramaid(current_values):
    current_differences = [current_values[i + 1] - current_values[i] for i in range(len(current_values) - 1)]
    pyramaid = [current_values]
    traversing_down = True

    while traversing_down:
        pyramaid.append(current_differences)

        if all(number == 0 for number in current_differences):
            traversing_down = False
        else:
            current_differences = [current_differences[i + 1] - current_differences[i] for i in range(len(current_differences) - 1)]  

    return pyramaid

def get_extrapolated_value(pyramaid, want_backwards_extrapolation=False):
    bubble_value = None  
    bubbling_index = 0 if want_backwards_extrapolation else -1

    for row_index in range(len(pyramaid) - 2, -1, -1):
        above_row = pyramaid[row_index]
        below_row = pyramaid[row_index + 1]

        if bubble_value is None:
            if want_backwards_extrapolation:
                bubble_value = above_row[bubbling_index] - below_row[bubbling_index]
            else:
                bubble_value = above_row[bubbling_index] + below_row[bubbling_index]
        else:
            if want_backwards_extrapolation:
                bubble_value = above_row[bubbling_index] - bubble_value
            else:
                bubble_value = bubble_value + above_row[bubbling_index]
    
    return bubble_value

# Part 1
extapolation_sum_p1 = 0

for history in histories:
    current_values = [int(number) for number in history.split(' ')]
    pyramaid = generate_pyramaid(current_values)
    extapolation_sum_p1 += get_extrapolated_value(pyramaid)

print(f'Part 1: {extapolation_sum_p1}')

# Part 2
extrapolation_sum_p2 = 0

for history in histories:
    current_values = [int(number) for number in history.split(' ')]
    pyramaid = generate_pyramaid(current_values)
    extrapolation_sum_p2 += get_extrapolated_value(pyramaid, want_backwards_extrapolation=True)

print(f'Part 2: {extrapolation_sum_p2}')