with open("day1_sonar_sweep/input.txt") as f:
    lines = f.read().splitlines()

lines = [int(x) for x in lines]

increasing_count = 0
for idx, line in enumerate(lines[:len(lines) - 1]):
    if line < lines[idx + 1]:
        increasing_count += 1

print(increasing_count)


# part two

increasing_count = 0
for idx, line in enumerate(lines[:len(lines) - 1]):
    if sum(lines[idx: idx + 2]) < sum(lines[idx + 1: idx + 3]):
        print(idx)
        print(sum(lines[idx: idx + 3]), sum(lines[idx + 1: idx + 4]))
        increasing_count += 1

print(increasing_count)
