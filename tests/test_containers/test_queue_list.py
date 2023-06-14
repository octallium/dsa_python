import pytest
from pytest import MonkeyPatch

from containers import QueueList as Queue

SIZE = 4


@pytest.fixture(scope="function")
def filled_queue() -> Queue[int]:
    q = Queue[int]()
    for i in range(SIZE):
        q.enqueue(i * 10)
    return q


@pytest.fixture(scope="function")
def partial_queue() -> Queue[int]:
    q = Queue[int]()
    for i in range(SIZE - 1):
        q.enqueue(i * 10)
    return q


class TestQueueList:
    def test_len(self, filled_queue: Queue[int]) -> None:
        assert len(filled_queue) == SIZE

    def test_empty(self, filled_queue: Queue[int]) -> None:
        assert filled_queue.isEmpty() == False
        assert Queue[str]().isEmpty() == True

    def test_dequeue(self, filled_queue: Queue[int]) -> None:
        for i in range(SIZE):
            assert filled_queue.dequeue() == (i * 10)
        assert Queue[int]().dequeue() == None

    def test_peek(self, filled_queue: Queue[int]) -> None:
        assert Queue[str]().peek() == None
        assert filled_queue.peek() == 0
        filled_queue.dequeue()
        assert filled_queue.peek() == 10

    def test_str(self, filled_queue: Queue[int]) -> None:
        assert str(filled_queue) == "Queue {0, 10, 20, 30}"
        filled_queue.dequeue()
        assert str(filled_queue) == "Queue {10, 20, 30}"

    def test_equal(self, filled_queue: Queue[int], partial_queue: Queue[int]) -> None:
        assert partial_queue != filled_queue
        partial_queue.enqueue(30)
        assert partial_queue == filled_queue

    def test_full(self, filled_queue: Queue[int], monkeypatch: MonkeyPatch) -> None:
        def raise_error() -> None:
            raise MemoryError

        monkeypatch.setattr(filled_queue, "isFull", raise_error, raising=True)
        with pytest.raises(MemoryError):
            filled_queue.isFull()
