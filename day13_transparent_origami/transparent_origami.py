import re
import numpy as np


def count_dots(paper):
    return np.count_nonzero(paper == 1)


def fold_up(paper, y):
    m_1 = paper[:y]
    m_2 = np.flip(paper[y + 1 :], axis=0)  # flip vertically to simulate the fold
    summed_matrix = m_1 + m_2
    summed_matrix[summed_matrix > 1] = 1
    return summed_matrix


def fold_left(paper, x):
    m_1, m_2 = np.hsplit(paper, [x])
    m_2 = np.flip(
        m_2[:, 1:], axis=1
    )  # since we split on the line, the line is included in m_2 -> remove that column and flip horizontally
    summed_matrix = m_1 + m_2
    summed_matrix[summed_matrix > 1] = 1
    return summed_matrix


def fold(paper, fold_instruction):
    if fold_instruction[0] == "x":
        folded_paper = fold_left(paper, int(fold_instruction[1]))
    elif fold_instruction[0] == "y":
        folded_paper = fold_up(paper, int(fold_instruction[1]))
    return folded_paper


with open("day13_transparent_origami/input.txt") as f:
    lines = f.read().splitlines()

rows = [row.split(",") for row in lines]

marks = [(int(row[0]), int(row[1])) for row in rows if len(row) == 2]
fold_instructions = [row[0] for row in rows if len(row) == 1 and "fold" in row[0]]

# dot is 0
# # is 1
# create empty matrix as grid
x_max = max([i[0] for i in marks]) + 1
y_max = max([i[1] for i in marks]) + 1
paper = np.zeros((y_max, x_max))

for mark in marks:
    paper[mark[1]][mark[0]] = 1

for instruction in fold_instructions[:1]:
    instruction = re.findall(r"(\w+)=(\d+)", instruction)[0]
    folded_paper = fold(paper, instruction)

print(folded_paper)
print(count_dots(folded_paper))
