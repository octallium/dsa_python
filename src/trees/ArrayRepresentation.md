# Array Representation of Binary Tree

## Example:


                     10
                /          \
               20           30
             /    \        /   \
           40      50    -1     60
          /  \     / \   / \   /  \
        70   -1  -1 -1 -1  -1 -1   80


    1. Values - [10, 20, 30, 40, 50, -1, 60, 70, -1, -1, -1, -1, -1, -1, 80]
    2. Index -  [0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14]

    Note: -1 Represents null value

## Index Positions:

    parent -> left, right
    ---------------------
    0 -> 1, 2
    1 -> 3, 4
    2 -> 5, 6
    3 -> 7, 8
    4 -> 9, 10
    5 -> 11, 12
    6 -> 13, 14

1. Node Indexes: 
   1. Parent: i
   2. Left: (i * 2) + 1
   3. Right: (i * 2) + 2