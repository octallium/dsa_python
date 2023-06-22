"""
Stack
-----
"""

from typing import Generic, TypeVar

T = TypeVar("T")

# ------------------------------------------------------------------


class Stack(Generic[T]):
    def __init__(self, size: int) -> None:
        """Stack using list."""

        self.__size = size
        self.__stk: list[T | None] = [None] * size
        self.__top = -1

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        return 0 if self.__top == -1 else self.__top + 1

    def __str__(self) -> str:
        return f"Stack {{{str([x for x in self.__stk if x != None][::-1])[1:-1]}}}"

    # API
    # ------------------------------------------------------------------

    def isEmpty(self) -> bool:
        return self.__top == -1

    def isFull(self) -> bool:
        return self.__top + 1 == self.__size

    def peek(self, pos: int) -> T | None:
        """Returns the element from the given position"""
        # Alternative - It can always return the top element

        if self.isEmpty() or pos < 0:
            raise Exception("Stack Underflow")

        if self.__top - pos + 1 < len(self):
            return self.__stk[self.__top - pos + 1]

        return None

    def push(self, el: T) -> None:
        """Pushes the element on the top of Stack"""

        if self.isFull():
            raise Exception("Stack Overflow")

        self.__top += 1
        self.__stk[self.__top] = el

    def pop(self) -> T | None:
        """Removes the element from the top of Stack"""

        if self.isEmpty():
            raise Exception("Stack Underflow")

        el = self.__stk[self.__top]
        self.__top -= 1
        return el
