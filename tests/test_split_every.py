import seqtk

from .common import CustomSequence


def test_split_every() -> None:
    seq = CustomSequence()
    assert len(seq) == 5
    new_seq = seqtk.split_every(2, seq)
    assert len(new_seq) == 3
    assert len(new_seq[0]) == 2
    assert len(new_seq[1]) == 2
    assert len(new_seq[2]) == 1
