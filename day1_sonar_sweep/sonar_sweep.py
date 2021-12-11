with open("day1_sonar_sweep/input.txt") as f:
    lines = f.read().splitlines()

lines = [int(x) for x in lines]

increasing_count = 0
for idx, line in enumerate(lines[:len(lines) - 1]):
    if line < lines[idx + 1]:
        increasing_count += 1

print(increasing_count)


# part two

with open("day1_sonar_sweep/input.txt") as f:
    lines = f.read().splitlines()

lines = [int(x) for x in lines]

increasing_count = 0
for idx, line in enumerate(lines[:len(lines) - 3]):
    if sum(lines[idx: idx + 2]) < sum(lines[idx + 1: idx + 3]):
        increasing_count += 1
    else: 
        print(sum(lines[idx: idx + 2]), sum(lines[idx + 1: idx + 3]))

print(increasing_count)
