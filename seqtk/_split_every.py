from typing import List, Sequence, TypeVar

from ._gather import gather

_T = TypeVar("_T")


def split_every(n: int, sequence: Sequence[_T]) -> List[Sequence[_T]]:
    indices_list: List[List[int]] = []
    for i in range(len(sequence)):
        if i % n == 0:
            indices_list.append([])
        indices_list[-1].append(i)

    return [gather(sequence, indices) for indices in indices_list]
