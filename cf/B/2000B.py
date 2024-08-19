import sys, threading, bisect, math, copy, itertools

from heapq import heappush, heappop, heapify
from functools import cmp_to_key as ctk, lru_cache
from collections import defaultdict, deque, Counter

readline = sys.stdin.readline
read = lambda : map(int, readline().split())
readstr = lambda : readline().rstrip()

# dfv 只能为基本数据类型
alloc = lambda dfv, *s: len(s) != 1 and [alloc(dfv, *s[1:]) for _ in range(int(s[0]))] or [dfv] * int(s[0])
show = lambda arr: print(" ".join(map(str, arr)))



def main():
    for _ in range(*read()):
        n, = read()
        arr = list(read())
        l = r = arr[0]
        res = 'YES'
        for i in range(1, n):
            if arr[i] == r + 1:
                r += 1
            elif arr[i] == l - 1:
                l -= 1
            else:
                res = 'NO'
                break
        print(res)



main()

# threading.stack_size((10 ** 8))
# t = threading.Thread(target=main)
# t.start()
# t.join()
