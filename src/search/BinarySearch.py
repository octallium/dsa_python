from typing import Sequence, TypeVar

T = TypeVar("T")


def binary_search(seq: Sequence[T], key: T) -> int | None:
    """
    Returns the index of `key` in `seq` using Binary Search.
    """

    try:
        return __binary_func(seq, key)
    except Exception:
        return None


def __binary_func(seq: Sequence[T], key: T) -> int | None:
    lo = 0
    hi = len(seq) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if seq[mid] == key:
            return mid
        elif seq[mid] < key:  # type:ignore
            # Note:
            # `T` | None < `T` will fail if `T` does not implement
            # comparison protocol.
            lo = mid + 1
        else:
            hi = mid - 1

    return None
