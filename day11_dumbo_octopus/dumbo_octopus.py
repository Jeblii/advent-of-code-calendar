with open("day11_dumbo_octopus/example_input.txt") as f:
    lines = f.read().splitlines()

rows = [[int(number) for number in row] for row in lines]
positions = dict()

# populate each position with the corresponding value
for i, row in enumerate(lines):
    for j, cell, in enumerate(row):
        positions[(i, j)] = cell


adjacents_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def flash(updated_positions):
    flashes = 0
    while not all(updated_positions.values()) < 9:
        for key, value in updated_positions.items():
            if value > 9:
                flashes += 1
                for adjacent in adjacents_cells:
                    adjacent_pos = tuple(map(sum, zip(key, adjacent)))
                # print(adjacent_pos)
                    # check if adjacent pos out of bounds
                    if (all(i > 0  for i in adjacent_pos)) & (all(i < 10  for i in adjacent_pos)):
                        updated_positions[adjacent_pos] += 1
                updated_positions[key] = 0
    return flashes, updated_positions

# assignment one
def update_step(positions: dict) -> dict:
    # energy level of each octopus increases by one
    # if energy level > 9 -> all adjacent octopus + 1 
    # if energy level > 9. reset back to 0
    print(positions)
    updated_positions = {k: int(v) +1 for (k,v) in positions.items()}
    n_flashes, post_flash_positions = flash(updated_positions)

    return n_flashes, post_flash_positions

flashes_count = 0 
for i in range(10):
    flashes, positions = update_step(positions)
    flashes_count += flashes
    
print(flashes_count)