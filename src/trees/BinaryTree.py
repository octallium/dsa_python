"""
Binary Tree
-----------
"""

from __future__ import annotations

from typing import Generic, Sequence, TypeVar

from containers import QueueList as Queue

T = TypeVar("T")

# ------------------------------------------------------------------


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        """Tree Node"""

        self.data: T = data
        self.left: Node[T] | None = None
        self.right: Node[T] | None = None

    def __str__(self) -> str:
        return str(self.data)


# ------------------------------------------------------------------


class BinaryTree(Generic[T]):
    def __init__(self) -> None:
        """Binary Tree"""

        self.__root: Node[T] | None = None

    def __len__(self) -> int:
        return self.count()

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, BinaryTree):
            return False
        if self is obj:
            return True
        return self.pre_order_traversal() == obj.pre_order_traversal()

    # ------------------------------------------------------------------

    @staticmethod
    def from_list(values: Sequence[T]) -> BinaryTree[T]:
        """Creates a Binary Tree from Array Representation"""

        i = left_idx = right_idx = 0

        tree = BinaryTree[T]()  # Create Binary Tree
        q = Queue[Node[T] | None]()  # Create Queue
        node = Node[T](values[i])

        tree.__root = node  # Set root node
        q.enqueue(node)  # Push root node

        while True:
            current: Node[T] | None = q.dequeue()  # current working node

            if current:
                # Get Indexes
                left_idx = (i * 2) + 1
                right_idx = (i * 2) + 2

                if right_idx >= len(values):
                    break

                # Create Left & Right Nodes
                left_node: Node[T] | None = (
                    Node[T](values[left_idx]) if values[left_idx] != -1 else None
                )
                right_node: Node[T] | None = (
                    Node[T](values[right_idx]) if values[right_idx] != -1 else None
                )

                # Set Left & Right Nodes
                if left_node:
                    current.left = left_node
                if right_node:
                    current.right = right_node

                # Uncomment below to debug
                # print(f"Current: {current}, Left: {left_node}, Right: {right_node}")

                # Push child nodes into the Queue
                q.enqueue(left_node)
                q.enqueue(right_node)

            i += 1  # Move to next node

        del q  # free queue
        return tree

    # ------------------------------------------------------------------

    def isEmpty(self) -> bool:
        return self.__root == None

    # Traversals
    # ------------------------------------------------------------------

    def pre_order_traversal(self) -> list[T]:
        """Return Nodes by Pre-Order (NLR) Traversal."""

        values: list[T] = []

        def pre_order_func(node: Node[T] | None) -> None:
            if node:
                values.append(node.data)
                pre_order_func(node.left)
                pre_order_func(node.right)

        pre_order_func(self.__root)
        return values

    def in_order_traversal(self) -> list[T]:
        """Return Nodes by In-Order (LNR) Traversal."""

        values: list[T] = []

        def in_order_func(node: Node[T] | None) -> None:
            if node:
                in_order_func(node.left)
                values.append(node.data)
                in_order_func(node.right)

        in_order_func(self.__root)
        return values

    def post_order_traversal(self) -> list[T]:
        """Return Nodes by Post-Order (LRN) Traversal."""

        values: list[T] = []

        def post_order_func(node: Node[T] | None) -> None:
            if node:
                post_order_func(node.left)
                post_order_func(node.right)
                values.append(node.data)

        post_order_func(self.__root)
        return values

    def level_order_traversal(self) -> list[T] | None:
        """Return Nodes by Level Order Traversal"""

        values: list[T] = []
        q = Queue[Node[T]]()

        if not self.__root:
            return None

        values.append(self.__root.data)
        q.enqueue(self.__root)

        while not q.isEmpty():
            current = q.dequeue()
            if current and current.left:
                values.append(current.left.data)
                q.enqueue(current.left)
            if current and current.right:
                values.append(current.right.data)
                q.enqueue(current.right)

        return values

    def count(self) -> int:
        """Returns the no of nodes"""

        def do_count(node: Node[T] | None) -> int:
            # Using Post Order Traversal
            if node:
                x = do_count(node.left)
                y = do_count(node.right)
                return x + y + 1
            return 0

        return do_count(self.__root)

    def count_leaf(self) -> int:
        """Returns the no of leaf nodes"""

        def do_count(node: Node[T] | None) -> int:
            # Using Post Order Traversal
            if node:
                x = do_count(node.left)
                y = do_count(node.right)
                # Count leaf only if no child nodes
                if not node.left and not node.right:
                    return x + y + 1
                else:
                    return x + y
            return 0

        return do_count(self.__root)

    def height(self) -> int:
        """Returns the Height of tree"""

        def do_height(node: Node[T] | None) -> int:
            if node:
                x = do_height(node.left)
                y = do_height(node.right)
                if x > y:
                    return x + 1
                else:
                    return y + 1
            return 0

        return do_height(self.__root)
