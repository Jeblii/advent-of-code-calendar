#Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits.
import dataclasses as dc

def parse_line(line: str) -> tuple:
    signal, output = line.split("|")
    return (signal, output)

with open("day8_seven_segment_search/input.txt") as f:
    line_segments = f.read().splitlines()


# assignment one
counter = 0
for line in line_segments:
    puzzle_line = parse_line(line) 
    counter += len([x for x in puzzle_line[1].split() if len(x) in [2, 3, 4, 7]])

# assignment two
@dc.dataclass
class Segment:
    a: str
    b: str
    c: str
    d: str
    e: str
    f: str
    g: str
    h: str

def decode_signal(signal: str) -> Segment:
    signals = signal.split()
    one = set([el for el in signals if len(el) == 2][0])
    seven = set([el for el in signals if len(el) == 3][0])
    four = set([el for el in signals if len(el) == 4][0])
    eight = set([el for el in signals if len(el) == 7][0])

    a = one.symmetric_difference(seven).pop()
    b_and_d = one.symmetric_difference(four)
    print(b_and_d)

    #print( four.union(seven).symmetric_difference()) 
    sorted_list = sorted(signals, key=len)
    
    pass

print(counter)

zero = {'a', 'b', 'c', 'e', 'f', 'g'}
one = {'c', 'f'}
two = {'a', 'c', 'd', 'e', 'g'}
three = {'a', 'c', 'd', 'f', 'g'}
four = {'b', 'c', 'd', 'f'}
five = {'a', 'b', 'd', 'f', 'g'}
six = {'a', 'b', 'd', 'e', 'f', 'g'}
seven = {'a', 'c', 'f'}
eight = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
nine = {'a', 'b', 'c', 'd', 'f', 'g'}

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
