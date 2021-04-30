# Sequence Tool Kit

`seqtk` provides various tools for [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence).

## Installation
```
pip install seqtk
```

## Documentation

### Mapping
Return a mapping of a function over the sequence.

#### Case1: Single sequence
Signature: `seqtk.map(func: Callable[[S], T], sequence: Sequence[S])`

Example:
```python
import seqtk
arr = [1, 2, 3]
view = seqtk.map(lambda v: v + 1, arr)
view[0]  # 2
```

#### Case2: Multiple sequences
Example (n=2):
```python
import seqtk
from typing import Tuple

def f(u: int, v: str) -> Tuple[int, str]:
  return u, v

arr0 = [1, 2, 3]
arr1 = ["a", "b", "c"]
view = seqtk.map(f, arr0, arr1)
view[0]  # (1, "a")
```

### Gather
Return a view on the sequence reordered by indices.

Signature: `seqtk.gather(sequence: Sequence[T], indices: Sequence[int])`

Example:
```python
import seqtk
arr = [1, 2, 3]
view = seqtk.gather(arr, [2, 0])
view[0]  # 3
```

### Concatenate
Return a view on the concatenated sequences.

Signature: `seqtk.concatenate(sequences: Sequence[Sequence[T]])`

Example:
```python
import seqtk
arr = [1, 2, 3]
view = seqtk.concatenate([arr, arr])
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
