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
        a, b = read(), read()
        # 每有一个端点不同就得多关一扇门，少于等于一个端点一样就只关一闪门
        print(max(min(b[1], a[1]) - max(a[0], b[0]) + (a[1] != b[1]) + (a[0] != b[0]), 1))




main()

# threading.stack_size((10 ** 8))
# t = threading.Thread(target=main)
# t.start()
# t.join()
