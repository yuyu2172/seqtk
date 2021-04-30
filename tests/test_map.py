from typing import Sequence

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
