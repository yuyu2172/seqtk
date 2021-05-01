import bisect
from typing import List, Sequence, TypeVar, Union, overload

from seqtk._helper import slice_to_indices

_T = TypeVar("_T")


class concatenate(Sequence[_T]):
    def __init__(self, sequences: Sequence[Sequence[_T]]):
        self._sequences = sequences
        self._cumulative_sizes = self._calculate_cumsum(sequences)

    @staticmethod
    def _calculate_cumsum(sequences: Sequence[Sequence[_T]]) -> List[int]:
        r = []
        s = 0
        for seq in sequences:
            seq_size = len(seq)
            r.append(seq_size + s)
            s += seq_size
        return r

    def __len__(self) -> int:
        return self._cumulative_sizes[-1]

    @overload
    def __getitem__(self, index: int) -> _T:
        ...

    @overload
    def __getitem__(self, index: slice) -> List[_T]:
        ...

    def __getitem__(self, index: Union[int, slice]) -> Union[_T, List[_T]]:
        if isinstance(index, slice):
            return [
                self._getitem_with_integer_index(i) for i in slice_to_indices(index)
            ]
        return self._getitem_with_integer_index(index)

    def _getitem_with_integer_index(self, index: int) -> _T:
        seq_index = bisect.bisect_right(self._cumulative_sizes, index)
        offset = self._cumulative_sizes[seq_index - 1] if seq_index > 0 else 0
        intra_seq_sample_index = index - offset
        return self._sequences[seq_index][intra_seq_sample_index]
