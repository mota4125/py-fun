from itertools import chain, combinations, permutations
from typing import Iterable, Any, List, Tuple

class Collection:
    def contains(self, s: Iterable, e: Any) -> int:
        return sum(1 for item in s if item == e)

    def zip(self, s: Iterable, p: Iterable) -> List[Tuple[Any, Any]]:
        return list(zip(s, p))

    def pset(self, s: Iterable) -> List[Tuple]:
        s = list(s)
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

    def perm(self, p: Iterable) -> List[Tuple]:
        return list(permutations(p))
