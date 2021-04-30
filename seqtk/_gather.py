from typing import List, Sequence, TypeVar, Union, overload

T = TypeVar("T")


class gather(Sequence[T]):
    def __init__(self, sequence: Sequence[T], indices: Sequence[int]):
        self._sequence = sequence
        self._indices = indices

    def __len__(self) -> int:
        return len(self._indices)

    @overload
    def __getitem__(self, index: int) -> T:
        ...

    @overload
    def __getitem__(self, index: slice) -> List[T]:
        ...

    def __getitem__(self, index: Union[int, slice]) -> Union[T, List[T]]:
        if isinstance(index, int):
            return self._sequence[self._indices[index]]
        return [self._sequence[i] for i in self._indices[index]]
