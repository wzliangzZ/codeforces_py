import sys, threading, bisect, math, copy, itertools

from heapq import heappush, heappop, heapify
from functools import cmp_to_key as ctk, lru_cache
from collections import defaultdict, deque, Counter

readline = sys.stdin.readline
read = lambda : list(map(int, readline().split()))
readstr = lambda : readline().rstrip()

# dfv 只能为基本数据类型
alloc = lambda dfv, *s: len(s) != 1 and [alloc(dfv, *s[1:]) for _ in range(int(s[0]))] or [dfv] * int(s[0])
show = lambda arr: print(" ".join(map(str, arr)))



def main():
    for _ in range(int(*read())):
        n, = read()
        arr = read()
        if n > 2: print('NO')
        elif abs(arr[0] - arr[1]) > 1: print('YES')
        else: print('NO')


main()

# threading.stack_size((10 ** 8))
# t = threading.Thread(target=main)
# t.start()
# t.join()
