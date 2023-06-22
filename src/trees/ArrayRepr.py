"""
Binary Tree In Array representation:
------------------------------------

Reference:
----------

1)

                     10
                /          \
               20           30
             /    \        /   \
           40      50    -1     60
          /  \     / \   / \   /  \
        70   -1  -1 -1 -1  -1 -1   80

        Array: [10, 20, 30, 40, 50, -1, 60, 70, -1, -1, -1, -1, -1, -1, 80]

2)

          8
        /   \
       3     5
      / \   / \
     4   9 7   2

    Array: [8, 3, 5, 4, 9, 7, 2]

"""

from typing import Sequence, TypeVar

T = TypeVar("T")

# ------------------------------------------------------------------


def print_nodes(values: Sequence[T]) -> None:
    """Prints Binary Tree Nodes from Array Representation"""

    i = left_idx = right_idx = 0
    parent: T | None = None
    left: T | None = None
    right: T | None = None

    while True:
        parent = values[i]

        if parent == -1:
            i += 1
            continue

        # Find Indexes
        left_idx = (i * 2) + 1
        right_idx = (i * 2) + 2

        # Check right index
        if right_idx >= len(values):
            break

        # Create Left and Right Nodes
        left = values[left_idx]
        right = values[right_idx]

        # Skip Nodes
        if right == -1:
            right = None
        if left == -1:
            left = None

        print(f"Parent: {parent}, Left: {left}, Right: {right}")

        i += 1
