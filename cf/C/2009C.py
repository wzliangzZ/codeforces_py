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
        x, y, k = read()
        x = x // k + (x % k != 0)
        y = y // k + (y % k != 0)
        if x > y:
            print((x - 1) * 2 + 1)
        else:
            print(y * 2)
        



main()

# threading.stack_size((10 ** 8))
# t = threading.Thread(target=main)
# t.start()
# t.join()
