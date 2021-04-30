from typing import Sequence, Tuple

import pytest
import seqtk

from .common import CustomSequence, Value


def test_map() -> None:
    seq = CustomSequence()

    def func(v: Value) -> float:
        return v.number

    new_seq = seqtk.map(func, seq)
    assert len(new_seq) == len(seq)
    list(new_seq)

    def sequence_consumer(seq: Sequence[float]) -> None:
        pass

    sequence_consumer(new_seq)

    def func_with_two_arguments(v: Value, u: Value) -> Tuple[float, float]:
        return v.number, u.number

    seq_two = seqtk.map(func_with_two_arguments, seq, seq)
    list(seq_two)

    def func_with_three_arguments(
        v: Value, u: Value, w: Value
    ) -> Tuple[float, float, float]:
        return v.number, u.number, w.number

    seq_three = seqtk.map(func_with_three_arguments, seq, seq, seq)
    list(seq_three)

    def func_with_four_arguments(
        v: Value, u: Value, w: Value, z: float
    ) -> Tuple[float, float, float, float]:
        return v.number, u.number, w.number, z

    # Type checker fails to detect error in this case.
    # `z` is declared as float, but Value is passed.
    seq_four = seqtk.map(func_with_four_arguments, seq, seq, seq, seq)
    list(seq_four)


def test_invalid() -> None:
    with pytest.raises(TypeError):
        seqtk.map(lambda x: "foo")  # type: ignore

    def f(x: int, y: int) -> None:
        pass

    with pytest.raises(ValueError):
        seqtk.map(f, [1, 2], [1])
