"""
QueueList:
---------
Queue implementation using Linked List.
"""

from typing import Generic, TypeVar

from containers.LinkedList import LinkedList

T = TypeVar("T")

# ------------------------------------------------------------------


class QueueList(Generic[T]):
    def __init__(self) -> None:
        """Queue using Linked List."""

        self.__que = LinkedList[T]()

    def __len__(self) -> int:
        return len(self.__que)

    def __str__(self) -> str:
        return "Queue" + str(self.__que)[11:]

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, QueueList):
            return False
        return self.__que == obj.__que

    # API
    # ------------------------------------------------------------------

    def isEmpty(self) -> bool:
        return self.__que.isEmpty()

    def isFull(self) -> bool:
        return self.__que.isFull()

    def enqueue(self, el: T) -> None:
        """Adds object at the back"""

        self.__que.append(el)

    def peek(self) -> T | None:
        """Returns first element"""

        return self.__que.head()

    def dequeue(self) -> T | None:
        """Removes element from front"""

        el = self.peek()
        tail = self.__que.tail()
        if tail:
            self.__que = tail
        else:
            self.__que = LinkedList[T]()
        return el
