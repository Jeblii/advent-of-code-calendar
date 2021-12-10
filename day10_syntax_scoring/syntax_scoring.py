with open("day10_syntax_scoring\input.txt") as f:
    lines = f.read().splitlines()

#print(lines)

chars = {
    '}' : '{',
    ']' : '[',
    ')' : '(',
    '>' : '<',
}
points = {
    ')': 3,
    ']': 57, 
    '}': 1197, 
    '>': 25137
}

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
#print(sum(chunks))

# assignment two

reverse_chars = {
    '{' : '}',
    '[' : ']',
    '(' : ')',
    '<' : '>',
}

points_completion = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def score_completion_string(completion_string: list) -> int:
    total_score = 0
    for char in completion_string:
        total_score *= 5
        total_score += points_completion[char]
    return total_score

def winning_score(score_list: list) -> int:
    return sorted(score_list)[len(score_list) // 2]

def autocomplete_line(line: str) -> int:
    chunk = []
    for char in line:
        #print(chunk)
        if char in opening_chars:
            chunk.append(char)
        elif not chunk or chunk.pop() != chars[char]:
            # corrupted
            chunk = None
            break
    return score_completion_string(reversed([reverse_chars[el] for el in chunk])) if chunk else None

scores = [autocomplete_line(line) for line in lines]
scores = [x for x in scores if x is not None]
print(sorted(scores))
print(winning_score(scores))