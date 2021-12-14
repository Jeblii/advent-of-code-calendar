with open("day14_extended_polymerization/example_input.txt") as f:
    lines = f.read().splitlines()

rows = [row.split(',') for row in lines]

polymer_template = rows[0][0]
pair_insertion_rules = rows[2:]

rules = dict()
for rule in pair_insertion_rules:
    a, b = rule[0].split('->')
    rules[a] = b

print(rules)