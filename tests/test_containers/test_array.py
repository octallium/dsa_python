import pytest

from containers import Array

CAPACITY = 4


@pytest.fixture(scope="function")
def filled_array() -> Array[int]:
    a = Array[int](4)
    for i in range(4):
        a.insert(i * 10)
    return a


class TestArray:
    def test_capacity(self, filled_array: Array[int]):
        assert filled_array.capacity == CAPACITY

    def test_len(self, filled_array: Array[int]) -> None:
        assert len(filled_array) == CAPACITY

    def test_isEmpty(
        self,
    ) -> None:
        assert True == Array[int](CAPACITY).isEmpty()

    def test_isFull(self, filled_array: Array[int]) -> None:
        assert True == filled_array.isFull()

    def test_delete(self, filled_array: Array[int]) -> None:
        for i in range(len(filled_array)):
            assert (i * 10) == filled_array.delete(i * 10)
        assert filled_array.isEmpty() == True

    def test_deleteAll(
        self,
    ) -> None:
        a = Array[int].from_list([10, 10, 20, 30])
        expected = Array[int].from_list([20, 30])
        a.delete_all(10)
        assert a == expected

    def test_find(self, filled_array: Array[int]) -> None:
        assert filled_array.find(30) == 3
        assert filled_array.find(25) == -1

    def test_equality(self, filled_array: Array[int]) -> None:
        assert filled_array == Array[int].from_list([0, 10, 20, 30])

    def test_map(self, filled_array: Array[int]) -> None:
        expected = Array[int].from_list([10, 20, 30, 40])
        assert filled_array.map(lambda x: x + 10) == expected

    def test_filter(self, filled_array: Array[int]) -> None:
        expected = Array[int].from_list([20, 30])
        assert filled_array.filter(lambda x: x >= 20) == expected

    def test_overflow(self, filled_array: Array[int]) -> None:
        with pytest.raises(Exception):
            filled_array.insert(40)

    def test_indexError(self, filled_array: Array[int]) -> None:
        with pytest.raises(IndexError):
            filled_array[5]

    def test_str(self, filled_array: Array[int]) -> None:
        assert str(filled_array) == "Array {0, 10, 20, 30}"

    def test_getItem(self, filled_array: Array[int]) -> None:
        assert filled_array[2] == 20

    def test_setItem(self, filled_array: Array[int]) -> None:
        filled_array[0] = 50
        assert filled_array[0] == 50
