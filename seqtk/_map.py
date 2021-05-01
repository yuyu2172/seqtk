from typing import Any, Callable, List, Sequence, TypeVar, Union, overload

from seqtk._helper import slice_to_indices

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_S = TypeVar("_S")


class map(Sequence[_S]):
    @overload
    def __init__(self, func: Callable[[_T1], _S], __seq1: Sequence[_T1]):
        ...

    @overload
    def __init__(
        self,
        func: Callable[[_T1, _T2], _S],
        __seq1: Sequence[_T1],
        __seq2: Sequence[_T2],
    ):
        ...

    @overload
    def __init__(
        self,
        func: Callable[[_T1, _T2, _T3], _S],
        __seq1: Sequence[_T1],
        __seq2: Sequence[_T2],
        __seq3: Sequence[_T3],
    ):
        ...

    @overload
    def __init__(
        self,
        func: Callable[..., _S],
        __seq1: Sequence[Any],
        __seq2: Sequence[Any],
        __seq3: Sequence[Any],
        __seq4: Sequence[Any],
        *sequences: Sequence[Any],
    ):
        ...

    def __init__(self, func: Any, *sequences: Any):
        super().__init__()
        if len(sequences) == 0:
            raise TypeError("map() must have at least two arguments")
        is_all_same_length = len(set(len(seq) for seq in sequences)) == 1
        if not is_all_same_length:
            raise ValueError("All seqeuences should have the same length.")
        self._length = len(sequences[0])
        self._func = func
        self._sequences = sequences

    def __len__(self) -> int:
        return self._length

    @overload
    def __getitem__(self, index: int) -> _S:
        ...

    @overload
    def __getitem__(self, index: slice) -> List[_S]:
        ...

    def __getitem__(self, index: Union[int, slice]) -> Any:
        if isinstance(index, slice):
            return [
                self._getitem_with_integer_index(i) for i in slice_to_indices(index)
            ]
        return self._getitem_with_integer_index(index)

    def _getitem_with_integer_index(self, index: int) -> Any:
        args = [seq[index] for seq in self._sequences]
        return self._func(*args)
