import sys, threading, bisect, math, copy, itertools

from heapq import heappush, heappop, heapify
from functools import cmp_to_key as ctk, lru_cache
from collections import defaultdict, deque, Counter

readline = sys.stdin.readline
read = lambda : map(int, readline().split())
readstr = lambda : readline().rstrip()

# dfv 只能为基本数据类型
alloc = lambda dfv, *s: len(s) != 1 and [alloc(dfv, *s[1:]) for _ in range(int(s[0]))] or [dfv] * int(s[0])
show = lambda arr: print("".join(map(str, arr)))



def main():
    for _ in range(*read()):
        n, = read()
        s = readstr()
        res = [''] * n
        dfd = defaultdict(int)
        for c in s:
            dfd[ord(c) - ord('a')] -= 1
        h = [(y, x) for (x, y) in dfd.items()]
        h.sort()
        i, j = 0, 0
        for __ in range(n):
            (cnt, val) = h[i]
            res[j] = chr(ord('a') + val)
            if cnt + 1 != 0:
                h[i] = (cnt + 1, val)
            else:
                i += 1
            j += 2
            if j >= n: j = 1
        show(res)


main()

# threading.stack_size((10 ** 8))
# t = threading.Thread(target=main)
# t.start()
# t.join()
