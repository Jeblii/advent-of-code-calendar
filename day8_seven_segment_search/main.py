#Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits.
import dataclasses as dc
from collections import Counter

def parse_line(line: str) -> tuple:
    signal, output = line.split("|")
    return (signal, output)

with open("day8_seven_segment_search/example_input.txt") as f:
    line_segments = f.read().splitlines()


# assignment one
counter = 0
for line in line_segments:
    puzzle_line = parse_line(line) 
    #print(puzzle_line[0].split())
    counter += len([x for x in puzzle_line[1].split() if len(x) in [2, 3, 4, 7]])

#print(counter)

# assignment two

reference = {
    8: 'acedgfb',
    5: 'cdfbe',
    2: 'gcdfa',
    3: 'fbcad',
    7: 'dab',
    9: 'cefabd',
    6: 'cdfgeb',
    4: 'eafb',
    0: 'cagedb',
    1: 'ab',
}

def decode_signal(signal: str) -> int:
    signals = signal.split()
    one = set([el for el in signals if len(el) == 2][0])
    four = set([el for el in signals if len(el) == 4][0])
    seven = set([el for el in signals if len(el) == 3][0])

    counter = Counter(puzzle_line[0])
    print(counter)
    a = one.symmetric_difference(seven).pop()
    c = [k for k, v in counter.items() if ((v == 8) and (v!=a)) ][0]
    e = [k for k, v in counter.items() if v == 4][0]
    b = [k for k, v in counter.items() if v == 6][0]
    f = [k for k, v in counter.items() if v == 9][0]
    print(four)
    print(b, c, f)
    print([el for el in four if el not in [b, c, f]])
    print('')

    #d = 
    #d = diff 0 and 8
    pass

for line in line_segments:
    puzzle_line = parse_line(line) 
    decode_signal(puzzle_line[0])

# 2 char always [one]
# 3 char always [seven]
# 4 char always [four]
# 5 char can be [two, three, five]
# 6 char can be [zero, six, nine]
# 7 char always [eight]

# one how to know which number is what - compare against number with one of c and f but not both [two, five]
#print(one.symmetric_difference(seven).pop())

# 4 digits: [e]
# 6 digits: [b] 
# 7 digits [d, g]
# 8 digits: [a, c]
# 9 digits: [f]
