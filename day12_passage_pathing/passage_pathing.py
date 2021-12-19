from itertools import combinations

with open("day12_passage_pathing/example_input.txt") as f:
    lines = f.read().splitlines()

rows = [row.split("-") for row in lines]
all_unique_chars = {x for l in rows for x in l}

# print(list(combinations(rows, len(all_unique_chars))))


def traverse_node(node, visited):
    if "end" not in node:
        print(node)
        print(
            [path for path in rows if (any(n in path for n in node)) and (path != node)]
        )
        possible_paths = [
            path for path in rows if (any(n in path for n in node)) and (path != node)
        ]
        # print(possible_paths)
        # for path in possible_paths:
        #     print(path)
        #     for point in node:
        #         if point.islower():
        #             visited.append(point)
        #     traverse_node(path, visited)

    return 1


def find_n_paths(rows, visited_small):
    n_path = 0
    start_nodes = [path for path in rows if "start" in path]
    end_nodes = [path for path in rows if "end" in path]
    path_nodes = [
        path for path in rows if path not in start_nodes and path not in end_nodes
    ]

    # visited_small.append(start_nodes)
    for node in start_nodes:
        traverse_node(node, visited_small)
        # possible_paths = [path for path in rows if (node[1] == path[0])]
        # print(possible_paths)
        # for path in possible_paths:

        #     print(path)


find_n_paths(rows, visited_small=[])
# for row in rows:
#     print(set(row))
