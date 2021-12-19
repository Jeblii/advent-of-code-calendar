import numpy as np
from collections import Counter


def binary_to_decimal(binary_n: str) -> int:
    return int(binary_n, 2)


# col [:, i]
# row [i,:]


def oxygen_generator_rating(matrix):
    # check from 1st - nth bit columns the most frequent number.
    #       if 1 most common: keep 1, if 0 most common: keep 0
    #       if 0 and 1 equally common: keep 1
    for i in range(matrix.shape[1]):
        col = matrix[:, i]
        # counts = np.bincount(col)
        # most_common = np.argmax(counts)
        counts = Counter(col)
        if counts[0] == counts[1]:
            most_common = 1
        else:
            most_common = max(counts, key=counts.get)
        matrix = np.array([row for row in matrix if row[i] == most_common])

    return matrix[0]


def co2_scrubber_rating(matrix):
    # check from 1st - nth bit columns the most frequent number.
    #       if 1 most common: keep 1, if 0 most common: keep 0
    #       if 0 and 1 equally common: keep 1
    for i in range(matrix.shape[1]):
        col = matrix[:, i]
        # counts = np.bincount(col)
        # most_common = np.argmax(counts)
        counts = Counter(col)
        if counts[0] == counts[1]:
            least_common = 0
        else:
            least_common = min(counts, key=counts.get)
        matrix = np.array([row for row in matrix if row[i] == least_common])

    return matrix[0]


def parse_ndarray_string(ndarray):
    res = "".join([str(el) for el in ndarray])
    return res


with open("day3_binary_diagnostic/input.txt") as f:
    lines = f.read().splitlines()

parsed_lines = [[int(c) for c in row] for row in lines]
matrix = np.array([np.array(xi) for xi in parsed_lines])

og_rating_binary = parse_ndarray_string(oxygen_generator_rating(matrix))
co2_rating_binary = parse_ndarray_string(co2_scrubber_rating(matrix))

print(binary_to_decimal(og_rating_binary) * binary_to_decimal(co2_rating_binary))
