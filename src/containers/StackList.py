"""
Stack
-----
"""

from typing import Generic, TypeVar

from containers.LinkedList import LinkedList

T = TypeVar("T")

# ------------------------------------------------------------------


class StackList(Generic[T]):
    def __init__(self) -> None:
        """Stack using Linked List."""

        self.__stk = LinkedList[T]()

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        return len(self.__stk)

    def __str__(self) -> str:
        values = [x.data for x in self.__stk][::-1]
        return f"Stack {{{str(values)[1:-1]}}}"

    # API
    # ------------------------------------------------------------------

    def isEmpty(self) -> bool:
        return self.__stk.isEmpty()

    def isFull(self) -> bool:
        return self.__stk.isFull()

    def peek(self) -> T | None:
        """Returns the element from the top position"""

        if self.isEmpty():
            raise Exception("Stack Underflow")

        return self.__stk.peek(len(self.__stk) - 1)

    def push(self, el: T) -> None:
        """Pushes the element on the top of Stack"""

        if self.isFull():
            raise Exception("Stack Overflow")

        self.__stk.append(el)

    def pop(self) -> T | None:
        """Removes the element from the top of Stack"""

        if self.isEmpty():
            raise Exception("Stack Underflow")

        return self.__stk.pop()
