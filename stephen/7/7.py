# python 1.py input.txt
import math
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

# 'J': 10,
card_order = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 0,
    'Q': 11,
    'K': 12,
    'A': 13
}

# 10: 'J',
card_rank_to_symbol = {
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: 'T',
    0: 'J',
    11: 'Q',
    12: 'K',
    13: 'A'
}


def parse_lines(lines):
    hands = []
    bids = []

    for line in lines:
        hands.append(line.split(' ')[0])
        bids.append(int(line.split(' ')[1]))

    return hands, bids


def determine_type(hand):
    characters_counted = []
    character_counts = []

    i = 0
    while i < 5:
        if characters_counted.count(hand[i]) == 0:
            characters_counted.append(hand[i])
            character_counts.append(hand.count(hand[i]))
        i += 1

    character_counts.sort(reverse=True)

    if character_counts[0] == 1:
        return 'high_card'
    if character_counts[0] == 5:
        return 'five_kind'
    if character_counts[0] == 4:
        return 'four_kind'
    if character_counts[0] == 2 and character_counts[1] == 2:
        return 'two_pair'
    if character_counts[0] == 2:
        return 'pair'
    if character_counts[0] == 3 and character_counts[1] == 2:
        return 'full_house'
    if character_counts[0] == 3:
        return 'three_kind'


'''
ignore jokers while getting the counts of other card types 
add count of jokers to highest character_count after sorting
'''
def determine_type_with_j(hand):
    characters_counted = []
    character_counts = []
    j_count = hand.count('J')

    i = 0
    while i < 5:
        if characters_counted.count(hand[i]) == 0 and hand[i] != 'J':
            characters_counted.append(hand[i])
            character_counts.append(hand.count(hand[i]))
        i += 1

    character_counts.sort(reverse=True)
    if len(character_counts) == 0:
        return 'five_kind'

    character_counts[0] += j_count

    print(hand)
    print(j_count)
    print(character_counts)

    if character_counts[0] == 1:
        return 'high_card'
    if character_counts[0] == 5:
        return 'five_kind'
    if character_counts[0] == 4:
        return 'four_kind'
    if character_counts[0] == 2 and character_counts[1] == 2:
        return 'two_pair'
    if character_counts[0] == 2:
        return 'pair'
    if character_counts[0] == 3 and character_counts[1] == 2:
        return 'full_house'
    if character_counts[0] == 3:
        return 'three_kind'


def sort_within_type(hands_group_unsorted):
    '''
    ['KK677', 'KTJJT']
    '''
    hands_converted_to_i = []
    for hand in hands_group_unsorted:
        hands_converted_to_i.append([convert_string_hand(hand)])

    converted_hands_sorted = sorted(hands_converted_to_i)

    type_hands_sorted = []
    for hand in converted_hands_sorted:
        type_hands_sorted.append(convert_int_hand(hand[0]))

    return type_hands_sorted


def convert_int_hand(hand):
    new_hand = ''
    for i in range(len(hand)):
        new_hand += card_rank_to_symbol[hand[i]]

    return new_hand


def convert_string_hand(hand):
    new_hand = []
    for l in hand:
        new_hand.append(card_order[l])

    return new_hand


if __name__ == "__main__":
    hands, bids = parse_lines(lines)
    hand_to_bids_hash = {}
    for i in range(len(hands)):
        hand_to_bids_hash[hands[i]] = bids[i]

    types_rank_map = {
        'five_kind': 6,
        'four_kind': 5, 
        'full_house': 4, 
        'three_kind': 3,
        'two_pair': 2,
        'pair': 1,
        'high_card': 0 
    }

    hands_grouped_unsorted = [[],[],[],[],[],[],[]]
    hands_sorted = []

    for hand in hands:
        hand_type = determine_type_with_j(hand)
        hands_grouped_unsorted[types_rank_map[hand_type]].append(hand)

    for i in range(len(hands_grouped_unsorted)):
        hands_sorted.append(sort_within_type(hands_grouped_unsorted[i]))

    print(hands_sorted)

    # print(hands_sorted)

    flattened_hands_sorted = [item for sublist in hands_sorted for item in sublist]

    # print(flattened_hands_sorted)

    total_winnings = 0

    for i in range(len(flattened_hands_sorted)):
        total_winnings += (i+1) * hand_to_bids_hash[flattened_hands_sorted[i]]

    print(total_winnings)
