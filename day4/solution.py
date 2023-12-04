from collections import Counter

with open('input.txt', 'r') as file:
    cards = file.read().splitlines()

def get_total_amount_of_common_numbers(card, card_index):
    cleaned_card =  " ".join([part.strip() for part in card.split(" ")]).replace(f"Card {card_index + 1}:", "")
    elf_numbers, your_numbers = cleaned_card.split(' | ')

    elf_numbers_set = set(int(number) for number in elf_numbers.split(" ") if number.strip().isnumeric())
    your_numbers_set = set(int(number) for number in your_numbers.split(" ") if number.strip().isnumeric())
    common_number_set = elf_numbers_set.intersection(your_numbers_set)

    return len(common_number_set)

def copy_cards(start_card_number, end_card_number, common_number_card_counts, card_number_counts):
    card_number_range = range(start_card_number, end_card_number + 1)
    if start_card_number not in card_number_range: return
    if end_card_number not in card_number_range: return

    for card_number in card_number_range:
        card_number_counts[card_number] += 1
        common_card_count = common_number_card_counts[card_number]

        new_card_number_start = card_number + 1
        new_card_number_end = new_card_number_start + (common_card_count - 1)
        copy_cards(new_card_number_start, new_card_number_end, common_number_card_counts, card_number_counts)



# Part 1
total_card_points = 0

for card_index, card in enumerate(cards):  
    common_amount = get_total_amount_of_common_numbers(card, card_index)

    if common_amount:
        card_score = 1

        for _ in range(common_amount - 1):
            card_score *= 2

        total_card_points += card_score

print(f"Part 1: {total_card_points}")

# Part 2
card_number_counts = Counter()
common_number_card_counts = {card_index + 1 : get_total_amount_of_common_numbers(card, card_index) for card_index, card in enumerate(cards)}

copy_cards(1, len(common_number_card_counts), common_number_card_counts, card_number_counts)


total_scratchcards = sum(card_number_counts.values())
print(f"Part 2: {total_scratchcards}")