from typing import List, Sequence, TypeVar, Union, overload

_T = TypeVar("_T")


class gather(Sequence[_T]):
    def __init__(self, sequence: Sequence[_T], indices: Sequence[int]):
        self._sequence = sequence
        self._indices = indices

    def __len__(self) -> int:
        return len(self._indices)

    @overload
    def __getitem__(self, index: int) -> _T:
        ...

    @overload
    def __getitem__(self, index: slice) -> List[_T]:
        ...

    def __getitem__(self, index: Union[int, slice]) -> Union[_T, List[_T]]:
        if isinstance(index, slice):
            return [self._sequence[i] for i in self._indices[index]]
        return self._sequence[self._indices[index]]
