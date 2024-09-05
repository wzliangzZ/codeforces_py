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
        up, low = [], []
        up_set, low_set = set(), set()
        for i in range(n):
            a, b = read()
            if b == 0:
                low.append(a)
                low_set.add(a)
            else:
                up.append(a)
                up_set.add(a)
        low.sort()
        up.sort()  
        n_low, n_up = len(low), len(up) 
        res = 0
        i, j = 0, 0
        while i < n_low and j < n_up:
            if low[i] < up[j]:
                res += (low[i] + 1 in up_set and low[i] - 1 in up_set)
                i += 1
            elif low[i] > up[j]:
                res += (up[j] + 1 in low_set and up[j] - 1 in low_set)
                j += 1
            else:
                res += n_low - 1 + n_up - 1
                res += (low[i] + 1 in up_set and low[i] - 1 in up_set)
                res += (up[j] + 1 in low_set and up[j] - 1 in low_set)
                i += 1
                j += 1
        print(res)



main()

# threading.stack_size((10 ** 8))
# t = threading.Thread(target=main)
# t.start()
# t.join()
