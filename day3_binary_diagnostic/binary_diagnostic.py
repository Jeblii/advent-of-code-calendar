def binary_to_decimal(binary_n: str) -> int:
    return int(binary_n, 2)


with open("day3_binary_diagnostic/example_input.txt") as f:
    lines = f.read().splitlines()

columns = list(map(list, zip(*lines)))

gamma_rate = "".join([max(set(col), key=col.count) for col in columns])
epsilon_rate = "".join([min(set(col), key=col.count) for col in columns])

print(binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate))

print(columns)
