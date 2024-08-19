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
        
        m, = read()
        for j in range(m):
            s = readstr()
            if len(s) != n:
                print('NO')
                continue
            res = 'YES'
            ctn, ntc = {}, {}
            for num, c in zip(arr, s):
                if num in ntc and ntc[num] != c:
                    res = 'NO'
                    break
                elif c in ctn and ctn[c] != num:
                    res = 'NO'
                    break
                ctn[c] = num
                ntc[num] = c
            print(res)


main()

# threading.stack_size((10 ** 8))
# t = threading.Thread(target=main)
# t.start()
# t.join()
