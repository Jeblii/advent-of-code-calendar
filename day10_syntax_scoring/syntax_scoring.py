with open("day10_syntax_scoring\input.txt") as f:
    lines = f.read().splitlines()

#print(lines)

chars = {
    '}' : '{',
    ']' : '[',
    ')' : '(',
    '>' : '<',
}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

opening_chars = ['{', '[', '(', '<']
closing_chars = ['}', ']', ')', '>']

def part_one(line):
    total = 0
    chunk = []
    for char in line:
        if char in opening_chars:
            chunk.append(char)
        elif chunk.pop() != chars[char]:
            total += points[char]
    return total

chunks = [part_one(line) for line in lines]
print(sum(chunks))
