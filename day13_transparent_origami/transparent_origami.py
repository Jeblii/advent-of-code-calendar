import re

with open("day13_transparent_origami/example_input.txt") as f:
    lines = f.read().splitlines()

rows = [row.split(',') for row in lines]

paper = [(int(row[0]), int(row[1])) for row in rows if len(row) == 2]
fold_instructions = [row[0] for row in rows if len(row) == 1 and 'fold' in row[0]]

positions = dict()

#for max x 
for i in range(max([i[0] for i in paper]) + 1):
    # for max y
    for j in range(max([i[1] for i in paper]) + 1):
        positions[(i, j)] = '.'

positions.update({k:'#' for k, v in positions.items() if k in paper})

def fold_up(paper, y):
    pass

def fold_left(paper, x):
    pass

def fold(paper, fold_instruction):
    if fold_instruction[0] :
        print('fold left')
    elif 'y' in fold_instruction:
        #for i in range(2, 4)
        print('fold up')

for instruction in fold_instructions:
    print(re.findall(r'(\w+)=(\d+)', instruction)[0])
    #print(fold(positions, instruction))