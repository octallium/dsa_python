import pytest
from pytest import MonkeyPatch

from containers import LinkedList


@pytest.fixture(scope="function")
def empty_list() -> LinkedList[int]:
    return LinkedList[int]()


@pytest.fixture(scope="function")
def filled_list() -> LinkedList[int]:
    ll = LinkedList[int]()
    for el in range(10, 50, 10):
        ll.append(el)
    return ll


class TestLinkedList:
    def test_len(
        self, empty_list: LinkedList[int], filled_list: LinkedList[int]
    ) -> None:
        assert len(empty_list) == 0
        assert len(filled_list) == 4

    def test_str(
        self, empty_list: LinkedList[int], filled_list: LinkedList[int]
    ) -> None:
        assert str(empty_list) == "Linked List {}"
        assert str(filled_list) == "Linked List {10, 20, 30, 40}"

    def test_contains(self, filled_list: LinkedList[int]) -> None:
        assert (20 in filled_list) == True
        assert (25 in filled_list) == False

    def test_from_list(self, filled_list: LinkedList[int]) -> None:
        assert filled_list == LinkedList[int].from_list([10, 20, 30, 40])

    def test_head(self, filled_list: LinkedList[int]) -> None:
        assert filled_list.head() == 10

    def test_insert_head(self, filled_list: LinkedList[int]) -> None:
        filled_list.insert_head(5)
        assert filled_list.head() == 5

    def test_tail(self, filled_list: LinkedList[int]) -> None:
        assert filled_list.tail() == LinkedList[int].from_list([20, 30, 40])

    def test_delete(
        self, empty_list: LinkedList[int], filled_list: LinkedList[int]
    ) -> None:
        assert empty_list.delete(10) == None
        assert filled_list.delete(10) == 10
        assert filled_list.delete(40) == 40
        assert filled_list.delete(40) == None

    def test_find(
        self, empty_list: LinkedList[int], filled_list: LinkedList[int]
    ) -> None:
        assert empty_list.find(10) == None
        assert filled_list.find(15) == None

    def test_insert(
        self, empty_list: LinkedList[int], filled_list: LinkedList[int]
    ) -> None:
        assert empty_list.insert(1, 15) == False
        assert empty_list.insert(0, 10) == True
        assert empty_list.head() == 10
        assert filled_list.insert(0, 5) == True
        assert filled_list.head() == 5
        assert len(filled_list) == 5
        assert filled_list.insert(10, 50) == False
        assert filled_list.insert(4, 50) == True
        assert len(filled_list) == 6

    def test_map(self, filled_list: LinkedList[int]) -> None:
        expected = LinkedList[int].from_list([20, 30, 40, 50])
        new_ll = LinkedList[int].map(filled_list, lambda x: x + 10)
        assert new_ll == expected

    def test_filter(self, filled_list: LinkedList[int]) -> None:
        expected = LinkedList[int].from_list([20, 30])
        new_ll = LinkedList[int].filter(filled_list, lambda x: x >= 20 and x < 40)
        assert new_ll == expected

    def test_full(self, filled_list: LinkedList[int], monkeypatch: MonkeyPatch) -> None:
        def raise_error() -> None:
            raise MemoryError

        monkeypatch.setattr(filled_list, "isFull", raise_error, raising=True)
        with pytest.raises(MemoryError):
            filled_list.isFull()
