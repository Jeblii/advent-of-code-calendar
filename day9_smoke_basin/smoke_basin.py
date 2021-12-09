from typing import List
import numpy as np

with open("day9_smoke_basin\input.txt") as f:
    rows = f.read().splitlines()
    rows = [list(line) for line in rows]

def plus_height(low_points:list) -> int:
    return sum([lp + 1 for lp in low_points])

def part_one(grid: List[List[str]]):
    low_points = []
    # travese horizontally
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            right = grid[i][j + 1] if j + 1 < len(line) else float('inf')
            left = grid[i][j - 1] if j > 0  else float('inf')
            above = grid[i - 1][j] if i > 0 else float('inf')
            below = grid[i + 1][j] if i + 1 < len(grid) else float('inf')
            if el < min(right, left, above, below):
                low_points.append(el)
            else:
                continue
    return low_points

rows = [[int(number) for number in row] for row in rows]

low_points = part_one(rows)
print(plus_height(low_points))
