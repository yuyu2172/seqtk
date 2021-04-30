# Sequence Tool Kit

`seqtk` provides various tools for [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence).

By using `seqtk`, you could declare data manipulation logic while deferring the actual data indexing.
This could be useful for data loading pipleines of machine learning libraries such as PyTorch's `torch.utils.data`.

## Installation
```
pip install seqtk
```

## Documentation

### Mapping
Returns a mapping of a function over the sequence.

#### Case1: Single sequence
Signature: `seqtk.map(func: Callable[[S], T], sequence: Sequence[S])`

Example:
```python
import seqtk
seq = [1, 2, 3]
view = seqtk.map(lambda v: v + 1, seq)
view[0]  # 2
```

#### Case2: Multiple sequences
Example (n=2):
```python
import seqtk
from typing import Tuple

def f(u: int, v: str) -> Tuple[int, str]:
  return u, v

seq0 = [1, 2, 3]
seq1 = ["a", "b", "c"]
view = seqtk.map(f, seq0, seq1)
view[0]  # (1, "a")
```

### Gather
Returns a view on the sequence reordered by indices.

Signature: `seqtk.gather(sequence: Sequence[T], indices: Sequence[int])`

Example:
```python
import seqtk
seq = [1, 2, 3]
view = seqtk.gather(seq, [2, 0])
view[0]  # 3
```

### Concatenate
Returns a view on the concatenated sequences.

Signature: `seqtk.concatenate(sequences: Sequence[Sequence[T]])`

Example:
```python
import seqtk
seq = [1, 2, 3]
view = seqtk.concatenate([seq, seq])
len(view)  # 6
```

## Development
### Test
```
pytest tests/
```

### Lint
```
pysen run lint
```
