with open("day11_dumbo_octopus/example_input.txt") as f:
    lines = f.read().splitlines()

rows = [[int(number) for number in row] for row in lines]
positions = dict()

# populate each position with the corresponding value
for i, row in enumerate(lines):
    for j, cell, in enumerate(row):
        positions[(i, j)] = cell


adjacents_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def flash(updated_positions, flashed):
    flashing = [key for key, value in updated_positions.items() if value > 9 and key not in flashed]

    if flashing:
        
        for key in flashing:
            flashed.append(key)

            for adjacent in adjacents_cells:
                adjacent_pos = tuple(map(sum, zip(key, adjacent)))
                # check if adjacent pos out of bounds
                if (all(i >= 0  for i in adjacent_pos)) & (all(i < 10  for i in adjacent_pos)):
                    updated_positions[adjacent_pos] += 1
        updated_positions = flash(updated_positions, flashed)

    return updated_positions

# assignment one
def update_step(positions: dict) -> dict:
    # energy level of each octopus increases by one
    # if energy level > 9 -> all adjacent octopus + 1 
    # if energy level > 9. reset back to 0
    updated_positions = {k: int(v) +1 for (k,v) in positions.items()}
    post_flash_positions = flash(updated_positions, flashed=[])
    n_flashes = len([val for key, val in post_flash_positions.items() if val > 9])
    post_flash_positions.update({p: 0 for p, val in post_flash_positions.items() if val > 9}) 
    return n_flashes, post_flash_positions

flashes_count = 0 
for i in range(100):
    flashes, positions = update_step(positions)
    print('after step', i + 1)
    print(flashes)
    print(positions)
    print('')
    flashes_count += flashes
    
print(flashes_count)

# part two
