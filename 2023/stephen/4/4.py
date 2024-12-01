# python 1.py input.txt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

'''
The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque covering already scratched off. Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|): a list of winning numbers and then a list of numbers you have. You organize the information into a table (your puzzle input).

As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list of winning numbers. The first match makes the card worth one point and each match after the first doubles the point value of that card.

For example:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

    Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
    Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
    Card 4 has one winning number (84), so it is worth 1 point.
    Card 5 has no winning numbers, so it is worth no points.
    Card 6 has no winning numbers, so it is worth no points.

So, in this example, the Elf's pile of scratchcards is worth 13 points
'''

def extract_line(line):
    winning_numbers = []
    player_numbers = []
    line = line.split(':')[1]
    wn = line.split('|')[0]
    wn = wn.split(' ')
    pn = line.split('|')[1]
    pn = pn.split(' ')
    for n in wn:
        if n.isdigit():
            winning_numbers.append(int(n.strip()))
    for n in pn:
        if n.isdigit():
            player_numbers.append(int(n.strip()))

    return winning_numbers, player_numbers


if __name__ == "__main__":
    # part 1
    points_total = 0
    for line in lines:
        winning_numbers, player_numbers = extract_line(line)

        winning_set = set(winning_numbers)
        player_numbers = set(player_numbers)

        intersection = winning_set & player_numbers

        if len(intersection) > 0:
            points_total += 2**(len(intersection)-1)
        
        # print('points total ' + str(points_total))

    # part 2
    card_copies_counts = [1]*len(lines)
    for index, line in enumerate(lines): 
        card_index = index
        winner_numbers, player_numbers = extract_line(line)

        winner_numbers_set = set(winner_numbers)
        player_numbers_set = set(player_numbers)
        
        winning_number_set = winner_numbers_set & player_numbers_set

        additional_cards_won = len(winning_number_set)

        for n in range(additional_cards_won):
            card_copies_counts[card_index + n + 1] += 1 * card_copies_counts[card_index]

        print('sum')
        print(sum(card_copies_counts))
