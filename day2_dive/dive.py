with open("day2_dive/input.txt") as f:
    lines = f.read().splitlines()

position = {
    "horizontal_pos": 0,
    "depth": 0,
    "aim": 0,
}


def adjust_position(instruction, pos):
    direction, unit = instruction.split()
    if direction == "forward":
        pos["horizontal_pos"] += int(unit)
    elif direction == "up":
        pos["depth"] -= int(unit)
    elif direction == "down":
        pos["depth"] += int(unit)
    return pos


def adjust_position2(instruction, pos):
    direction, unit = instruction.split()
    if direction == "forward":
        pos["horizontal_pos"] += int(unit)
        pos["depth"] += pos["aim"] * int(unit)
    elif direction == "up":
        pos["aim"] -= int(unit)
    elif direction == "down":
        pos["aim"] += int(unit)
    return pos


for line in lines:
    position = adjust_position2(line, position)

print(position)
# part one
print(position["horizontal_pos"] * position["depth"])
