import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional
T = TypeVar('T')

class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a: Optional[List[T]] = None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        self.size = len(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other) -> bool:
        return list(self) == list(other)
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int]:
        "Find the bucket and position which x should be inserted. self must not be empty."
        for a in self.a:
            if x <= a[-1]: break
        return (a, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a, i = self._position(x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a, i = self._position(x)
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
    
    def _pop(self, a: List[T], i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a: self._build()
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return self._pop(a, i)
        else:
            for a in self.a:
                if i < len(a): return self._pop(a, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

n,k,q = map(int,input().split())


mset_A = SortedMultiset()
mset_B = SortedMultiset()

for i in range(n):
  if i < k:
    mset_A.add(0)
  else:
    mset_B.add(0)


# 
A = [0] * n
for i in range(q):
  x,y = map(int,input().split())
  # A[x-1] 番目のものを集合Aから取り除いて集合Bに入れる
  # yを集合Aに入れる

  if mset_A.discard(A[x-1]) != True:
     mset_B.discard(A[x-1])
  mset_A.add(y)
  
  A[x-1]  = y
  # 集合Aの一番小さい値より集合Bの一番大きな値が大きければ入れ替える
  if mset_A[0] < mset_B[-1] and len(mset_A) == 2:
    rm = mset_B[-1]
    # print(rm,"入れ替えます")
    mset_A.add(rm)
    mset_B.discard(rm)
    

  # 集合Aの数がkを超えたら、一番小さい値をBに入れる
  
  if len(mset_A) > k:
    # print("kを超えた")
    rm = mset_A[0]
    # print(rm,"を削除します")
    mset_B.add(rm)
    mset_A.discard(rm)
    
  if len(mset_A) < k:
    # print("kを下回った",mset_A)
    ad = mset_B[-1]
    # print(ad,"を足します")
    mset_A.add(ad)
    mset_B.discard(ad)

  if len(mset_A) == k:
    # print("問題なし")
    pass
  
  # print(A)
  # print(mset_A,mset_B,"最大は",sum(mset_A))
  # print("--------------------------------------")
  print(sum(mset_A))









# 長さNのA[]が与えられる
# 
# f():
#   Aを降順にソートしたものをBとし
#   f(A) = B1 + B2 + Bk とする

# Q回行う
# A[x] = y


# [5, 0, 0, 0] -> 5
# [5, 1, 0, 0] -> 6
# [5, 1, 3, 0] -> 8 
# [5, 1, 3, 2] -> 8
# [5, 10, 3, 2]-> 15
# [0, 10, 3, 2]-> 13
# [0, 10, 3, 0]-> 13
# [0, 10, 1, 0]-> 11
# [0, 0, 1, 0] -> 1
# [0, 0, 0, 0] -> 0


# マルチセット
# 理解度D
# わからん