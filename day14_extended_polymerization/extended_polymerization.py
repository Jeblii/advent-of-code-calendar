from collections import Counter

with open("day14_extended_polymerization/example_input.txt") as f:
    lines = f.read().splitlines()

rows = [row.split(",") for row in lines]

polymer_template = rows[0][0]
pair_insertion_rules = rows[2:]

rules = dict()
for rule in pair_insertion_rules:
    a, b = rule[0].split("->")
    rules[a.strip()] = b.strip()  # strip to remove whitespaces


# find pairs
# find new pairs
# return counter of pairs


def part_two(polymer_counter):
    # pairs
    pairs = [k for (k, _) in polymer_counter.items()]
    # find new pairs
    new_pairs = []
    for pair in pairs:
        new_pairs.append(pair[0] + rules[pair])
        new_pairs.append(rules[pair] + pair[1])

    # make new counter of pairs
    new_pair_counter = Counter(new_pairs)
    print(new_pair_counter)
    return new_pair_counter


print(rules)
pairs = []
for i in range(0, len(polymer_template) - 1):
    pairs.append(polymer_template[i : i + 2])
pair_counter = Counter(pairs)

for i in range(10):
    pair_counter = part_two(pair_counter)

print(pair_counter)
