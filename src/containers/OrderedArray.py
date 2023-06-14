"""
Array:
-----
Fixed sized `Array` implementation using list.

Class Methods
-------------
1. from_list

Instance Methods
----------------
1. isFull
2. isEmpty
3. insert
4. find
5. delete
6. delete_all
7. map
8. filter

"""

from __future__ import annotations

from typing import Any, Callable, Generator, Generic, TypeVar

T = TypeVar("T")

# ------------------------------------------------------------------


class OrderedArray(Generic[T]):
    def __init__(self, capacity: int) -> None:
        """
        Array:
        -----
        Fixed sized `array`.

        Attributes
        ----------
        capacity: int
                  The maximum capacity of array
        """

        self.__capacity = capacity
        self.__size = 0
        self.__arr: list[T | None] = [None] * capacity
        self.__start = 0

    # Instance Properties
    # ------------------------------------------------------------------

    @property
    def capacity(self) -> int:
        return self.__capacity

    # ------------------------------------------------------------------

    @classmethod
    def from_list(cls, arr: list[T | None]) -> OrderedArray[T]:
        if not isinstance(arr, list):
            raise TypeError(f"expected a list, received: {type(arr)}")

        capacity = len(arr)
        c: OrderedArray[T] = OrderedArray(capacity)
        c.__size = capacity
        c.__arr = arr
        return c

    # ------------------------------------------------------------------

    def __str__(self) -> str:
        return f"Ordered Array {{{str([self.__arr[x] for x in range(self.__size)])[1:-1]}}}"

    def __len__(self) -> int:
        return self.__size

    def __bool__(self) -> bool:
        return bool(self.__arr)

    def __getitem__(self, index: int) -> T | None:
        return self.__arr[index] if self._validIndexOrThrowError(index) else None

    def __setitem__(self, index: int, value: T) -> None:
        raise NotImplementedError("Cannot set custom values in Ordered Array")

    def __iter__(self) -> Generator[T | None, Any, Any]:
        while self.__start < self.__size:
            yield self.__arr[self.__start]
            self.__start += 1
        self.__start = 0

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, OrderedArray):
            return False
        return self.__arr == obj.__arr

    # Helper Functions
    # ------------------------------------------------------------------

    def _validIndexOrThrowError(self, index: int) -> bool:
        if index < 0 or index >= self.__size:
            raise IndexError("list index out of range")
        return True

    def _shiftLeft(self, start: int) -> None:
        """Shift elements to the left by 1"""

        if not self.isEmpty():
            stop = self.__size - 1
            self._shift(start, stop)

    def _shiftRight(self, stop: int) -> None:
        """Shift elements to the right by 1"""

        if not self.isFull():
            start = self.__size
            self._shift(start, stop, -1)

    def _shift(self, start: int, stop: int, step=1) -> None:
        """Shifts elements by 1 in either right or left"""

        for i in range(start, stop, step):
            if step == -1:
                # Shift Right
                self.__arr[i] = self.__arr[i - 1]
            else:
                # Shift Left
                self.__arr[i] = self.__arr[i + 1]

        self.__arr[stop] = None
        self.__size -= step

    # API
    # ------------------------------------------------------------------

    def isFull(self) -> bool:
        return self.__size >= self.__capacity

    def isEmpty(self) -> bool:
        return True if self.__size == 0 else False

    def find(self, key: T) -> int:
        """Find index of the given object using binary search"""

        lo = 0
        hi = self.__size - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.__arr[mid] == key:
                return mid
            elif self.__arr[mid] < key:  # type:ignore
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

    def insert(self, el: T) -> None:
        """Inserts an element at the end of Array"""

        if self.isFull():
            raise Exception("Array overflow")

        # Steps
        # 1. find index
        # 2. shift elements
        # 3. insert element

        idx = self.find(el)
        self._shiftRight(idx)
        self.__arr[idx] = el

    def delete(self, obj: T) -> T | bool:
        """Deletes the first occurrence of object"""

        el: T | None = None
        idx = self.find(obj)
        if idx < self.__size and self.__arr[idx] == obj:
            el = self.__arr[idx]
            self._shiftLeft(idx)

        return el if el else False

    def delete_all(self, obj: T) -> None:
        """Deletes all occurrence of object"""

        self.__arr = [x for x in self.__arr if x != obj]
        self.__size = len(self.__arr)

    # Functional API
    # ------------------------------------------------------------------

    def map(self, func: Callable[[T | None], Any]) -> OrderedArray[T]:
        """Applies the func to all elements in array and returns a new array"""

        return OrderedArray.from_list([func(x) for x in self.__arr])

    def filter(self, predicate: Callable[[T | None], bool]) -> OrderedArray[T]:
        """Filters the array with the predicate and returns a new array"""

        return OrderedArray.from_list([x for x in self.__arr if predicate(x)])
