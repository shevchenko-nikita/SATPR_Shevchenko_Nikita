import itertools
import numpy as np

distances = np.array(
    [
        [68, 72, 75, 83],
        [56, 60, 58, 63],
        [38, 40, 35, 45],
        [47, 42, 40, 45]
     ]
)

bases = [0, 1, 2, 3]
consumers = [0, 1, 2, 3]

all_permutations = list(itertools.permutations(consumers))
alternative = []
min_total_distance = float("inf")

for perm in all_permutations:
    current_distance = 0

    for base, consumer in zip(bases, perm):
        current_distance += distances[base][consumer]

    if current_distance == min_total_distance:
        alternative.append(perm)

    if current_distance < min_total_distance:
        min_total_distance = current_distance
        alternative.clear()
        alternative.append(perm)

print("Value:", min_total_distance)
print("All optimal permutation:")
for alternative in alternative:
    for base in alternative:
        base += 1
        print(base, end=" ")
    print()