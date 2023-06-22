import pytest

from trees import BinaryTree

ARRAY1 = [10, 20, 30, 40, 50, -1, 60, 70, -1, -1, -1, -1, -1, -1, 80]
ARRAY2 = [8, 3, 5, 4, 9, 7, 2]


@pytest.fixture(scope="function")
def tree() -> BinaryTree[int]:
    return BinaryTree[int].from_list(ARRAY1)


class TestBinaryTree:
    def test_empty(self, tree: BinaryTree[int]) -> None:
        assert tree.isEmpty() == False
        assert BinaryTree[str]().isEmpty() == True

    def test_len(self, tree: BinaryTree[int]) -> None:
        assert len(tree) == 8

    def test_count(self, tree: BinaryTree[int]) -> None:
        assert tree.count() == 8

    def test_eq(self, tree: BinaryTree[int]) -> None:
        assert tree == BinaryTree[int].from_list(ARRAY1)
        assert tree != BinaryTree[int].from_list(ARRAY2)

    def test_pre_order(self, tree: BinaryTree[int]) -> None:
        tree2 = BinaryTree[int].from_list(ARRAY2)

        assert tree.pre_order_traversal() == [10, 20, 40, 70, 50, 30, 60, 80]
        assert tree2.pre_order_traversal() == [8, 3, 4, 9, 5, 7, 2]

    def test_in_order(self, tree: BinaryTree[int]) -> None:
        tree2 = BinaryTree[int].from_list(ARRAY2)

        assert tree.in_order_traversal() == [70, 40, 20, 50, 10, 30, 60, 80]
        assert tree2.in_order_traversal() == [4, 3, 9, 8, 7, 5, 2]

    def test_post_order(self, tree: BinaryTree[int]) -> None:
        tree2 = BinaryTree[int].from_list(ARRAY2)

        assert tree.post_order_traversal() == [70, 40, 50, 20, 80, 60, 30, 10]
        assert tree2.post_order_traversal() == [4, 9, 3, 7, 2, 5, 8]

    def test_level_order(self, tree: BinaryTree[int]) -> None:
        tree2 = BinaryTree[int].from_list(ARRAY2)

        assert tree.level_order_traversal() == [10, 20, 30, 40, 50, 60, 70, 80]
        assert tree2.level_order_traversal() == [8, 3, 5, 4, 9, 7, 2]

    def test_count_leaf(self, tree: BinaryTree[int]) -> None:
        tree2 = BinaryTree[int].from_list(ARRAY2)

        assert tree.count_leaf() == 3
        assert tree2.count_leaf() == 4

    def test_height(self, tree: BinaryTree[int]) -> None:
        assert tree.height() == 4
