#二分探索


# 基本 ------------------------------------------------------------------------
def binary_search(data, value):
  left = 0            
  right = len(data) - 1
  # 左側が左側より右に来たら終了
  while left <= right:
        mid = (left + right) // 2   
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        elif data[mid] > value:
            right = mid - 1
            
  return -1          

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 90))

# ------------------------------------------------------------------------
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k

def solve1():
    # 15 47
    # 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    
    left = 0
    right = n-1

    while left<=right:
        mid = (left + right) // 2
        # 真ん中を確認する
        if A[mid] == k:
           print(mid+1)
           break
        elif A[mid] < k:
            # kは真ん中より大きいのでレフト移動する
            left = mid + 1

        elif A[mid] > k:
            # kは真ん中より小さいのでrightを移動する
            right = mid - 1
            
  
solve1()

def solve2():
    # x以下の個数を求める
   
    n = int(input())
    A = list(map(int,input().split()))
    q = int(input())
    A.sort()
    print(A)
    X = []
    for i in range(q):
        x = int(input())
        print(bisect.bisect_left(A,x))
   
solve2()
# ------------------------------------------------------------------------
# bisectを使った二分探索
import bisect 
def bisect():
    # bisect.bisect_left(a, x)   # aのリストに対して値xを二分探索して、左側の挿入点を返す
    # bisect.bisect_right(a, x)  # aのリストに対して値xを二分探索して、右側の挿入点を返す
    # bisect.bisect(a, x)        # bisect_right(a, x)と同様
    # bisect.insort_left(a, x)   # ソートされた順序に保ちつつ挿入する
    # bisect.insort_right(a, x)  # ソートされた順序に保ちつつ挿入する、insort_leftと似ている
    # bisect.insort(a, x)        # ソートされた順序に保ちつつ挿入する、insort_leftと似ている
    A = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    x = 30
    print("xより小さいやつ",bisect.bisect_left(A,x))
    print("xより大きいやつ",bisect.bisect_right(A,x))
    # 配列に値を挿入する left,right違いわからん
    bisect.insort_left(A, 1)
    bisect.insort_right(A,2)
    bisect.insort(A, 3)

# ------------------------------------------------------------------------
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l
class Printer:
    # 4 10
    # 1 2 3 4

    # mid秒以下か判別する
    # mid秒で何枚印刷されているかを見る
    def check(mid,n,k,A):
        print(mid,"秒")

        # mid秒で印刷できる枚数
        sum = 0
        for i in range(n):
            sum += mid // A[i]
        if sum >= k:
            return True
        else:
            return False

    def solve():
        n,k = map(int,input().split())
        A = list(map(int,input().split()))

        # 答えで二分探索するときは,「x以上か」や「x以下か」などの時に使う
        left = 0
        right = 10 ** 9

        while left < right: 
            mid = (left + right) // 2
            # mid秒までにk枚印刷できるかどうかを確認する
            Answer = Printer.check(mid,n,k,A)
            
            if Answer:
                right = mid
            else:
                left = mid + 1

        print(left)
Printer.solve()


# N以下の数を求める
# 未満の数字を返すときはleftを返せばok
A = [1,5,6,7,8,9,10,12]

def cnt(n):
    left, right = 0,len(A)
    
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] <= n:
            left = mid
        else:
            right = mid            
    return right
  
print(cnt(5)) # -> 2



