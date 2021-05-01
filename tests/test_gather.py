import numpy as np
import seqtk

from .common import CustomSequence


def test_gather() -> None:
    seq = CustomSequence()
    indices = [2, 0]
    new_seq = seqtk.gather(seq, indices)
    assert len(new_seq) == len(indices)
    assert new_seq[0] == seq[indices[0]]
    assert new_seq[1] == seq[indices[1]]
    list(new_seq)

    new_seq[np.int64(1)]
