import sys

ordering_rules = []
updates = []

with open(sys.argv[1]) as f:
    for line in f.readlines():
        if line.__contains__('|'):
            ordering_rules.append(
                [int(n) for n in line.strip().split('|')]
            )

        if line.__contains__((',')):
            updates.append(
                [int(n) for n in line.strip().split(',')]
            )

afters = {}
befores = {}

for ordering in ordering_rules:
    if not afters.get(ordering[0], ''):
        afters[ordering[0]] = {ordering[1]}
    else:
        afters[ordering[0]].add(ordering[1])

    if not befores.get(ordering[1], ''):
        befores[ordering[1]] = {ordering[0]}
    else:
        befores[ordering[1]].add(ordering[0])


def check_update(update):
    for i, j in enumerate(update):
        if i == len(update):
            return None

        nums_before = set(update[:i])
        nums_after = set(update[i+1:])

        if afters.get(j, '') and afters[j].intersection(nums_before):
            return None
        elif befores.get(j, '') and befores[j].intersection(nums_after):
            return None

    return update[int((len(update)-1)/2)]

valid_midpoints = []
for i in range(0, len(updates)):
    valid_midpoints.append(check_update(updates[i]))


sum = 0
for n in valid_midpoints:
    if n:
        sum += n
print(f"sum: {sum}")


def fix_update(update): 
    for i, j in enumerate(update):
        if i == len(update):
            return None

        nums_before = set(update[:i])
        nums_after = set(update[i+1:])

        if afters.get(j, '') and afters[j].intersection(nums_before):
            intersection = afters[j].intersection(nums_before)
            min_i = len(update)
            for n in intersection:
                if update.index(n) < min_i:
                    min_i = update.index(n)

            update[i], update[min_i] = update[min_i], update[i]
            return update

        elif befores.get(j, '') and befores[j].intersection(nums_after):
            intersection = befores[j].intersection(nums_after)
            max_i = 0
            for n in intersection:
                if update.index(n) > max_i:
                    max_i = update.index(n)

            update[i], update[max_i] = update[max_i], update[i]
            return update

    return update[int((len(update)-1)/2)]


fixed_midpoints = []
for i in range(0, len(valid_midpoints)):
    if valid_midpoints[i] is not None:
        continue

    valid = False
    update = updates[i]
    while not valid:
        update = fix_update(update)
        check = check_update(update)
        if check:
            fixed_midpoints.append(check)
            valid = True

sum = 0
for midpoint in fixed_midpoints:
    sum += midpoint
print(f"sum: {sum}")
