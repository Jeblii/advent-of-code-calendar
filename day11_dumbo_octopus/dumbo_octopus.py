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

# from itertools import product
# from collections import Counter


# FILENAME = '../data/d11'


# def neighborhood(x, y): 
#     return [(x + a, y + b) for a, b in product((-1, 0, 1), repeat=2) if (a, b) != (0, 0)]


# def flash(H, flashed): 
#     flashing = [p for p, val in H.items() if val > 9 and p not in flashed]    
#     if flashing: 
#         for p in flashing: 
#             H.update({q: H[q] + 1 for q in neighborhood(*p) if q in H.keys()}) 
#         flash(H, flashing + flashed)


# def step(H): 
#     H.update({p: val + 1 for p, val in H.items()}) 
#     flash(H, list())         
#     H.update({p: 0 for p, val in H.items() if val > 9}) 
#     return H


# with open(FILENAME, 'r') as f: 
#     H = dict() 
#     for y, line in enumerate(f):
#         for x, val in enumerate(line.strip()): 
#             H[x, y] = int(val)

# # PART 1
# tot_flashes, steps_num = 0, 0 
# while steps_num < 100: 
#     steps_num += 1 
#     tot_flashes += Counter(step(H).values())[0] 
# print(tot_flashes)

# # PART 2
# while Counter(step(H).values())[0] != len(H): 
#     steps_num += 1 
# print(steps_num + 1)