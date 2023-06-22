"""
Linked List
-----------
"""

from __future__ import annotations

from typing import Any, Callable, Generator, Generic, Sequence, TypeVar

T = TypeVar("T")


# Node
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.next: Node | None = None
        self.data = data

    def __str__(self) -> str:
        return f"Node {{Data: {self.data}, Next: {self.next}}}"

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Node):
            return False
        return self.data == obj.data


# Linked List
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        """
        Linked List
        """
        self.__first: Node[T] | None = None
        self.__last: Node[T] | None = self.__first

    # ------------------------------------------------------------------

    def __str__(self) -> str:
        current = self.__first
        values: list[T] = []
        while current:
            values.append(current.data)
            current = current.next
        return f"Linked List {{{str(values)[1:-1]}}}"

    def __iter__(self) -> Generator[Node[T], Any, Any]:
        current = self.__first
        while current:
            yield current
            current = current.next

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, LinkedList):
            return False

        n = self.__first
        m = obj.__first

        while n and m:
            if n != m:
                break
            n = n.next
            m = m.next

        return True if n == m else False

    def __len__(self) -> int:
        count = 0
        if self.__first:
            for _ in self:
                count += 1
        return count

    def __contains__(self, key: T) -> bool:
        if self.isEmpty():
            return False

        for node in self:
            if node.data == key:
                return True
        return False

    def __add__(self, ll: LinkedList[T]) -> LinkedList[T]:
        if not isinstance(ll, LinkedList):
            raise TypeError(f"Expected Linked List, received type: {type(ll)}")

        if self.__last and ll.__first:
            self.__last.next = ll.__first
            self.__last = ll.__last
        return self

    # ------------------------------------------------------------------

    @classmethod
    def from_list(cls, seq: Sequence[T]) -> LinkedList[T]:
        """Creates a Linked List from a sequence"""

        l = LinkedList[T]()
        for el in seq:
            l.append(el)
        return l

    # API
    # ------------------------------------------------------------------

    def isEmpty(self) -> bool:
        return self.__first == None

    def isFull(self) -> bool:
        full = False
        try:
            _ = Node(None)
        except MemoryError:
            full = True
        return full

    def append(self, el: T) -> None:
        """Adds an object at the back"""

        n = Node(el)
        if not self.__first:
            self.__first = self.__last = n
        elif self.__last:
            self.__last.next = n
            self.__last = self.__last.next

    def insert_head(self, el: T) -> None:
        """Inserts an object at the head"""

        node = Node[T](el)
        if self.__first:
            node.next = self.__first
            self.__first = node
        else:
            self.__first = self.__last = node

    def head(self) -> T | None:
        """Returns first element from the Linked List"""

        if self.__first:
            return self.__first.data
        else:
            return None

    def tail(self) -> LinkedList[T] | None:
        """Returns tail from the Linked List"""

        if self.__first:
            ll = LinkedList[T]()
            ll.__first = self.__first.next
            ll.__last = self.__last
            return ll
        return None

    def insert(self, pos: int, value: T) -> bool:
        """Inserts an object at the given position"""

        isInserted = False

        if pos < 0 or pos > len(self):
            return isInserted

        if pos == 0:
            self.insert_head(value)
            # isInserted = True
        else:
            new_node = Node[T](value)
            follower: Node[T] | None = None
            current = self.__first

            for _ in range(pos):
                follower = current
                current = current.next  # type:ignore

            follower.next = new_node  # type:ignore
            new_node.next = current

            if self.__last == follower:  # move last if required
                self.__last = follower.next  # type:ignore

        isInserted = True
        return isInserted

    def find(self, key: T) -> Node[T] | None:
        """Finds a node for the given key"""

        current: Node[T] | None = None
        for node in self:
            if node.data == key:
                current = node
        return current

    def delete(self, key: T) -> T | None:
        """Delete the first matching key from Linked List"""

        if self.isEmpty():
            return None

        follower: Node[T] | None = None
        current = self.__first
        el: T | None = None

        while current:
            if current.data == key:
                if not follower:  # if we find match on the first node
                    if self.__first:
                        el = self.__first.data
                    self.__first = self.__first.next  # type:ignore
                else:  # if we find match on any other node
                    el = current.data
                    follower.next = current.next
                break
            follower = current
            current = current.next

        return el

    def reverse(self) -> LinkedList[T]:
        """Reverse the Linked List"""

        ll = LinkedList[T]()
        for node in self:
            ll.insert_head(node.data)
        return ll

    def pop(self) -> T | None:
        """Removes the last node and returns the data"""

        if not self.__first:
            raise Exception("Linked List Underflow")

        el: Node[T] | None = None

        if len(self) == 1:
            el = self.__first
            self.__first = self.__last = None
            return el.data

        current = self.__first

        while True:
            if current.next == self.__last:
                el = current.next
                self.__last = current
                current.next = None
                break
            if current.next:
                current = current.next

        return el.data if el else None

    def peek(self, pos: int) -> T | None:
        """Returns data from the given node position"""

        if pos < 0:
            raise Exception("Linked List Underflow")
        if pos > len(self) - 1:
            raise Exception("Linked List Overflow")

        current = self.__first

        for _ in range(pos):
            if current and current.next:
                current = current.next

        return current.data if current else None

    # Functional API
    # ------------------------------------------------------------------

    @staticmethod
    def map(ll: LinkedList[T], func: Callable[[T], Any]) -> LinkedList[T]:
        """Applies the func to all the elements in Linked List"""

        new_ll = LinkedList[T]()
        for node in ll:
            new_ll.append(func(node.data))
        return new_ll

    @staticmethod
    def filter(ll: LinkedList[T], predicate: Callable[[T], bool]) -> LinkedList[T]:
        """Filters the Linked List using the predicate"""

        new_ll = LinkedList[T]()
        for node in ll:
            if predicate(node.data) == True:
                new_ll.append(node.data)
        return new_ll
