from dataclasses import dataclass
from typing import List, Sequence, Union, overload


@dataclass
class Value:
    number: float
    text: str


class CustomSequence(Sequence[Value]):
    def __len__(self) -> int:
        return 5

    @overload
    def __getitem__(self, index: int) -> Value:
        ...

    @overload
    def __getitem__(self, index: slice) -> List[Value]:
        ...

    def __getitem__(self, index: Union[int, slice]) -> Union[Value, List[Value]]:
        def integer_to_value(i: int) -> Value:
            if not (0 <= i < len(self)):
                raise IndexError
            return Value(i, text=str(i))

        if isinstance(index, slice):
            indices = list(range(index.stop))[index]
            return [integer_to_value(i) for i in indices]
        return integer_to_value(index)
