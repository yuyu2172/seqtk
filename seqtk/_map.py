from typing import Callable, List, Sequence, TypeVar, Union, overload

_map = map


S = TypeVar("S")
T = TypeVar("T")


class map(Sequence[T]):
    def __init__(self, func: Callable[[S], T], sequence: Sequence[S]) -> None:
        super().__init__()
        self._func = func
        self._sequence = sequence

    def __len__(self) -> int:
        return len(self._sequence)

    @overload
    def __getitem__(self, index: int) -> T:
        ...

    @overload
    def __getitem__(self, index: slice) -> List[T]:
        ...

    def __getitem__(self, index: Union[int, slice]) -> Union[T, List[T]]:
        if isinstance(index, int):
            return self._func(self._sequence[index])
        return list(_map(self._func, self._sequence[index]))
