import seqtk

from .common import CustomSequence


def test_concatenate() -> None:
    seq = CustomSequence()
    new_seq = seqtk.concatenate([seq, seq])

    assert len(new_seq) == len(seq) * 2
    for i in range(len(new_seq)):
        assert new_seq[i] == seq[i % len(seq)]

    s = slice(0, 3)
    assert new_seq[s] == seq[s]
