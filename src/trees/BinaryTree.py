"""
Binary Tree:
------------
1. Nodes - {0, 1, 2}

Terms:
------
1. Nodes (n)
2. Edge 
3. Height (h)
4. Leaf - {0}
5. Degree - No of child nodes

Binary Tree:
------------
1. Child Nodes: {0, 1, 2}

2. For Height:
    1. Min Nodes: n - 1
    2. Max Nodes: log2(n + 1) 

3. For Nodes:
    1. Min Height: h + 1
    2. Max Height: 2^(h+1) - 1

Strict Tree:
------------
1. Child Nodes: {0, 2}

2. For Height:
    1. Min Nodes: n = 2h + 1
    2. Max Nodes: n = 2^(h+1) - 1

3. For Nodes:
    1. Min Height: h = log2(n + 1) - 1
    2. Max Height: h = (n - 1) / 2

    log2(n + 1) - 1 <= h <= (n + 1) / 2

4. Internal {1, 2} & External Nodes {0}:
    1. Internal Node {1, 2}
    2. External Node {0}
    3. No external nodes: e = i + 1

Strict M-ary Tree:
-----------------
1. Nodes: {0, m}

2. Height:
    1. Min h = (n - 1) / m
    2. Max h = log m (n (m - 1) + 1) - 1

3. Nodes:
    1. Min: n = mh + 1
    2. Max: n = m^(h+1) / (m - 1)

4. Internal vs External Node: e = (m - 1) i + 1

Array Representation:
---------------------
1. element - i
2. left child - i * 2
3. right child - (i * 2) + 1
4. parent - ⌊i / 2⌋

Traversal:
---------

1. Pre-oder: NLR
2. In-order: LNR
3. Post order: LRN
4. Level order
"""
