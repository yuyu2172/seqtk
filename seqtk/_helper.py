from typing import List


def slice_to_indices(s: slice) -> List[int]:
    return list(range(s.stop))[s]
