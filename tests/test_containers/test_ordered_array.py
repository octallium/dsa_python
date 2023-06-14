import pytest

from containers import OrderedArray

CAPACITY = 4


@pytest.fixture(scope="function")
def filled_array() -> OrderedArray[int]:
    a = OrderedArray[int](4)
    values = [10, 0, 30, 20]
    for i in values:
        a.insert(i)
    return a


class TestOrderedArray:
    def test_capacity(self, filled_array: OrderedArray[int]):
        assert filled_array.capacity == CAPACITY

    def test_len(self, filled_array: OrderedArray[int]) -> None:
        assert len(filled_array) == CAPACITY

    def test_isEmpty(
        self,
    ) -> None:
        assert True == OrderedArray[int](CAPACITY).isEmpty()

    def test_isFull(self, filled_array: OrderedArray[int]) -> None:
        assert True == filled_array.isFull()

    def test_delete(self, filled_array: OrderedArray[int]) -> None:
        expected = OrderedArray[int].from_list([0, 10, 30, None])
        assert filled_array.delete(20) == 20
        assert filled_array == expected

    def test_insert_position(self, filled_array: OrderedArray[int]) -> None:
        filled_array.delete(20)
        filled_array.insert(25)
        assert filled_array.find(25) == 2

    def test_deleteAll(
        self,
    ) -> None:
        a = OrderedArray[int].from_list([10, 10, 20, 30])
        expected = OrderedArray[int].from_list([20, 30])
        a.delete_all(10)
        assert a == expected

    def test_find(self, filled_array: OrderedArray[int]) -> None:
        assert filled_array.find(30) == 3

    def test_find_right_lo(self, filled_array: OrderedArray[int]) -> None:
        assert filled_array.find(25) == 3

    def test_equality(self, filled_array: OrderedArray[int]) -> None:
        assert filled_array == OrderedArray[int].from_list([0, 10, 20, 30])

    def test_map(self, filled_array: OrderedArray[int]) -> None:
        expected = OrderedArray[int].from_list([10, 20, 30, 40])
        assert filled_array.map(lambda x: x + 10) == expected

    def test_filter(self, filled_array: OrderedArray[int]) -> None:
        expected = OrderedArray[int].from_list([20, 30])
        assert filled_array.filter(lambda x: x >= 20) == expected

    def test_overflow(self, filled_array: OrderedArray[int]) -> None:
        with pytest.raises(Exception):
            filled_array.insert(40)

    def test_indexError(self, filled_array: OrderedArray[int]) -> None:
        with pytest.raises(IndexError):
            filled_array[5]

    def test_str(self, filled_array: OrderedArray[int]) -> None:
        assert str(filled_array) == "Ordered Array {0, 10, 20, 30}"

    def test_getItem(self, filled_array: OrderedArray[int]) -> None:
        assert filled_array[2] == 20

    def test_setItem(self, filled_array: OrderedArray[int]) -> None:
        with pytest.raises(NotImplementedError):
            filled_array[1] = 0
