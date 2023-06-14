"""
Circular Queue:
-----
Circular Queue implementation

"""

from typing import Generic, TypeVar

T = TypeVar("T")

# ------------------------------------------------------------------


class CircularQueue(Generic[T]):
    def __init__(self, size: int) -> None:
        """
        Circular Queue
        --------------
        Queue using lists.

        Arguments:
        ----------
        size: int
              Size of the queue
        """

        self.__size = size
        self.__front = -1
        self.__rear = -1
        self.__que: list[T | None] = [None] * size

    # ------------------------------------------------------------------

    def __str__(self) -> str:
        values: list[T | None] = []

        if not self.isEmpty():
            start = self.__front
            stop = self.__rear

            while start != stop:
                values.append(self.__que[start])
                start = (start + 1) % self.__size
            # Add the last element
            values.append(self.__que[start])

        return f"Circular Queue {{{str(values)[1:-1]}}}"

    def __len__(self) -> int:
        return len(self.__que)

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, CircularQueue):
            return False
        return self.__que == obj.__que

    # Helper Functions
    # ------------------------------------------------------------------

    def _nextRearIndex(self) -> int:
        """Returns the next rear index"""

        return (self.__rear + 1) % self.__size

    def _nextFrontIndex(self) -> int:
        """Returns the next front index"""

        return (self.__front + 1) % self.__size

    def _resetIndex(self) -> None:
        """Reset front and rear to -1"""

        self.__front = self.__rear = -1

    # API
    # ------------------------------------------------------------------

    def isFull(self) -> bool:
        return (self.__rear + 1) % self.__size == self.__front

    def isEmpty(self) -> bool:
        return self.__rear == self.__front == -1

    def enqueue(self, el: T) -> None:
        """Add an element to the rear of queue"""

        if self.isFull():
            raise Exception("Queue Overflow")

        if self.isEmpty():
            self.__front += 1

        self.__rear = self._nextRearIndex()
        self.__que[self.__rear] = el

    def dequeue(self) -> T | None:
        """Removes an element from the front"""

        if self.isEmpty():
            raise Exception("Queue Underflow")

        el = self.__que[self.__front]
        self.__que[self.__front] = None

        if self.__front == self.__rear:
            self._resetIndex()
        else:
            self.__front = self._nextFrontIndex()

        return el

    def peek(self) -> T | None:
        """Returns the object at front"""

        return None if self.isEmpty() else self.__que[self.__front]
