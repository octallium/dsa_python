import pytest

from containers import Stack

SIZE = 4


@pytest.fixture(scope="function")
def filled_stack() -> Stack[int]:
    s = Stack[int](SIZE)
    for i in range(SIZE):
        s.push(i * 10)
    return s


class TestStack:
    def test_full(self, filled_stack: Stack[int]) -> None:
        assert filled_stack.isFull() == True
        assert filled_stack.isEmpty() == False

    def test_empty(self) -> None:
        assert Stack[int](SIZE).isEmpty() == True

    def test_len(self, filled_stack: Stack[int]) -> None:
        assert len(filled_stack) == SIZE

    def test_peek(self, filled_stack: Stack[int]) -> None:
        assert filled_stack.peek(1) == 30
        assert filled_stack.peek(4) == 0

    def test_pop(self, filled_stack: Stack[int]) -> None:
        assert filled_stack.pop() == 30
        assert filled_stack.pop() == 20

    def test_push(self) -> None:
        s = Stack[str](SIZE)
        s.push("a")
        assert s.isEmpty() == False
        assert s.pop() == "a"

    def test_str(self, filled_stack: Stack[int]) -> None:
        assert str(filled_stack) == "Stack {30, 20, 10, 0}"
