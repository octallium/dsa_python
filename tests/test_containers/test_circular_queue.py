import pytest

from containers import CircularQueue

SIZE = 4


@pytest.fixture(scope="function")
def filled_queue() -> CircularQueue[int]:
    q = CircularQueue[int](SIZE)
    for i in range(SIZE):
        q.enqueue(i * 10)
    return q


@pytest.fixture(scope="function")
def partial_queue() -> CircularQueue[int]:
    q = CircularQueue[int](SIZE)
    for i in range(SIZE - 1):
        q.enqueue(i * 10)
    return q


class TestCircularQueue:
    def test_len(self, filled_queue: CircularQueue[int]) -> None:
        assert len(filled_queue) == SIZE

    def test_full(
        self, filled_queue: CircularQueue[int], partial_queue: CircularQueue[int]
    ) -> None:
        assert partial_queue.isFull() == False
        assert filled_queue.isFull() == True
        filled_queue.dequeue()
        assert filled_queue.isFull() == False

    def test_empty(self, filled_queue: CircularQueue[int]) -> None:
        assert filled_queue.isEmpty() == False
        assert CircularQueue[str](SIZE).isEmpty() == True

    def test_dequeue(self, filled_queue: CircularQueue[int]) -> None:
        for i in range(SIZE):
            assert filled_queue.dequeue() == (i * 10)

    def test_enqueue(
        self, filled_queue: CircularQueue[int], partial_queue: CircularQueue[int]
    ) -> None:
        assert filled_queue.isFull() == True
        filled_queue.dequeue()
        assert filled_queue.isFull() == False
        assert partial_queue.isFull() == False
        filled_queue.enqueue(40)
        partial_queue.enqueue(40)
        assert filled_queue.isFull() == True
        assert partial_queue.isFull() == True

    def test_peek(self, filled_queue: CircularQueue[int]) -> None:
        assert CircularQueue[str](SIZE).peek() == None
        assert filled_queue.peek() == 0
        filled_queue.dequeue()
        assert filled_queue.peek() == 10

    def test_str(self, filled_queue: CircularQueue[int]) -> None:
        assert str(filled_queue) == "Circular Queue {0, 10, 20, 30}"
        filled_queue.dequeue()
        filled_queue.enqueue(40)
        assert str(filled_queue) == "Circular Queue {10, 20, 30, 40}"

    def test_equal(
        self, filled_queue: CircularQueue[int], partial_queue: CircularQueue[int]
    ) -> None:
        assert partial_queue != filled_queue
        partial_queue.enqueue(30)
        assert partial_queue == filled_queue

    def test_underflow(self) -> None:
        with pytest.raises(Exception):
            CircularQueue[int]().dequeue()

    def test_overflow(self, filled_queue: CircularQueue[int]) -> None:
        with pytest.raises(Exception):
            filled_queue.enqueue(50)
