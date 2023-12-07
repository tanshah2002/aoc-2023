from collections import Counter
from functools import cmp_to_key
import sys

with open('input.txt', 'r') as file:
    hands_data = []
    lines = file.read().splitlines()

    for line in lines:
        hand, bid_amount = line.split(' ')
        hands_data.append((hand, int(bid_amount)))

HAND_TYPE_ORDERING = ['five-of-kind', 'four-of-kind', 'full-house', 'three-of-kind', 'two-pair', 'one-pair', 'high-card']
HAND_LABEL_ORDERING = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
HAND_LABEL_ORDERING_JOKER = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
HAND_TYPE_COUNT_TUPLES = {
    'five-of-kind': (5, ),
    'four-of-kind': (1, 4),
    'full-house': (2, 3),
    'three-of-kind': (1, 1, 3),
    'two-pair': (1, 2, 2),
    'one-pair': (1, 1, 1, 2),
    'high-card': (1, 1, 1, 1, 1),
}

is_five_of_kind = lambda hand: get_tuple_of_label_counts(hand) == (5, )
is_four_of_kind = lambda hand: get_tuple_of_label_counts(hand) == (1, 4)
is_full_house = lambda hand: get_tuple_of_label_counts(hand) == (2, 3)
is_three_of_kind = lambda hand: get_tuple_of_label_counts(hand) == (1, 1, 3)
is_two_pair = lambda hand: get_tuple_of_label_counts(hand) == (1, 2, 2)
is_one_pair = lambda hand: get_tuple_of_label_counts(hand) == (1, 1, 1, 2)
is_high_card = lambda hand: get_tuple_of_label_counts(hand) == (1, 1, 1, 1, 1)

def compute_best_hand_type_with_joker(hand):
    label_counts_with_no_joker = get_tuple_of_label_counts(hand.replace('J', '')) 
    final_label_counts_with_no_joker = list(label_counts_with_no_joker if label_counts_with_no_joker else (0, ))
    joker_count = hand.count('J')   
    final_label_counts_with_no_joker[-1] += joker_count 
    final_label_counts_with_no_joker = tuple(sorted(final_label_counts_with_no_joker))

    for hand_type, count_tuple in HAND_TYPE_COUNT_TUPLES.items():
        if count_tuple == final_label_counts_with_no_joker:
            return hand_type

    return 'unknown-type'


def get_tuple_of_label_counts(hand):
    label_counts = Counter(hand)
    return tuple(sorted(label_counts.values()))

def identify_hand_type(hand, playing_joker_game=False):
    if playing_joker_game: return compute_best_hand_type_with_joker(hand)
    if is_five_of_kind(hand): return 'five-of-kind'
    if is_four_of_kind(hand): return 'four-of-kind'
    if is_full_house(hand): return 'full-house'
    if is_three_of_kind(hand): return 'three-of-kind'
    if is_two_pair(hand): return 'two-pair'
    if is_one_pair(hand): return 'one-pair'     
    if is_high_card(hand): return 'high-card'

    return 'unknown-type'

def compare_hands(hand_a_data, hand_b_data, playing_joker_game=False):
    hand_a, _ = hand_a_data
    hand_b, _ = hand_b_data
    game_label_ordering = HAND_LABEL_ORDERING_JOKER if playing_joker_game else HAND_LABEL_ORDERING

    hand_a_type_index = HAND_TYPE_ORDERING.index(identify_hand_type(hand_a, playing_joker_game))
    hand_b_type_index = HAND_TYPE_ORDERING.index(identify_hand_type(hand_b, playing_joker_game))

    if hand_a_type_index < hand_b_type_index: return 1
    if hand_a_type_index > hand_b_type_index: return -1

    for hand_a_label, hand_b_label in zip(hand_a, hand_b):
        if hand_a_label != hand_b_label:
            hand_a_label_index = game_label_ordering.index(hand_a_label)
            hand_b_label_index = game_label_ordering.index(hand_b_label)

            if hand_a_label_index < hand_b_label_index: return 1
            else: return -1

    return 0

def get_total_winnings(hands_data, playing_joker_game=False):
    hand_cmp_fn = cmp_to_key(lambda hand_a_data, hand_b_data: compare_hands(hand_a_data, hand_b_data, True)) if playing_joker_game else cmp_to_key(compare_hands)
    sorted_hands_data = list(sorted(hands_data, key=hand_cmp_fn))
    total_winnings = 0

    for index, hand_data in enumerate(sorted_hands_data):
        rank = index + 1
        _, bid_amount = hand_data
        total_winnings += rank * bid_amount

    return total_winnings

# Part 1
p1_winnings = get_total_winnings(hands_data)
print(f'Part 1: {p1_winnings}')

# Part 2
p2_winnings = get_total_winnings(hands_data, True)
print(f'Part 2: {p2_winnings}')

