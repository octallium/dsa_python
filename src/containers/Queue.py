"""
Queue:
-----
Queue implementation

"""

from typing import Generic, TypeVar

T = TypeVar("T")

# ------------------------------------------------------------------


class Queue(Generic[T]):
    def __init__(self, size: int) -> None:
        """
        Queue
        -----
        Queue implementation using list.

        Arguments:
        ----------
        size: int
              Size of the queue
        """

        self.__size = size
        self.__front = -1  # -1 indicates null position, not last index
        self.__rear = -1
        self.__que: list[T | None] = [None] * size

    # ------------------------------------------------------------------

    def __str__(self) -> str:
        values = []
        if not self.isEmpty():
            values = [self.__que[x] for x in range(self.__front, self.__rear + 1)]
        return f"Queue {{{str(values)[1:-1]}}}"

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Queue):
            return False
        return self.__que == obj.__que

    def __len__(self) -> int:
        return len(self.__que)

    # API
    # ------------------------------------------------------------------

    def isFull(self) -> bool:
        return self.__rear == self.__size - 1

    def isEmpty(self) -> bool:
        return self.__front == -1

    def enqueue(self, el: T) -> None:
        """Add an element to the rear of queue"""

        if self.isFull():
            raise Exception("Queue Overflow")
        if self.isEmpty():
            self.__front += 1
        self.__rear += 1
        self.__que[self.__rear] = el

    def dequeue(self) -> T | None:
        """Removes an element from the front"""

        if self.isEmpty():
            raise Exception("Queue Underflow")
        el = self.__que[self.__front]
        self.__que[self.__front] = None
        self.__front += 1  # Increment front
        return el

    def peek(self) -> T | None:
        """Returns the object at front"""

        return None if self.isEmpty() else self.__que[self.__front]
