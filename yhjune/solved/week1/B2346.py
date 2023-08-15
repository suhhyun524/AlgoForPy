# https://www.acmicpc.net/problem/2346 풍선 터뜨리기
# 

import sys
import collections
input = sys.stdin.readline
bal = dict()
deque = collections.deque
start = 1

n = int(input().split())
list = list(map(int, input().split()))

for i in range(n):
    bal.update({i:list[i]})
    deque.append(list[i])

while start <= n :
    