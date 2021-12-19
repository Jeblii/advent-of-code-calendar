from typing import Tuple
import dataclasses as dc
import numpy as np
import itertools
from collections import defaultdict


@dc.dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int


def parse_line(line: str) -> Line:
    line1, line2 = line.split("->")
    line1_x, line1_y = line1.split(",")
    line2_x, line2_y = line2.split(",")
    return Line(x1=int(line1_x), y1=int(line1_y), x2=int(line2_x), y2=int(line2_y))


def draw_lines(lines: list) -> dict:
    grid = defaultdict(int)
    for line in lines:
        # vertical
        if line.x1 == line.x2:
            for i in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
                grid[(line.x1, i)] += 1
        # horizontal
        elif line.y1 == line.y2:
            for j in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
                grid[(j, line.y1)] += 1
        # part2
        # diagonal
        else:
            # rule for only exactly 45 degree means that the x and y coordinate shift the exact same distance
            if abs(line.x1 - line.x2) == abs(line.y1 - line.y2):
                x = 1 if line.x2 > line.x1 else -1
                y = 1 if line.y2 > line.y1 else -1
                for i in range(abs(line.x2 - line.x1) + 1):
                    grid[(line.x1 + i * x, line.y1 + i * y)] += 1

    return grid


with open("day5_hydrothermal_venture/input.txt") as f:
    line_segments = f.read().splitlines()

lines = [parse_line(line) for line in line_segments]

grid = draw_lines(lines)

print(sum([1 if v > 1 else 0 for v in grid.values()]))
