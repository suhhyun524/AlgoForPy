# https://www.acmicpc.net/problem/2346 풍선 터뜨리기

# 덱, 
# 로테이트

import sys
import collections
input = sys.stdin.readline
bal = dict()
deque = collections.deque
target, count = 1

n = int(input().split())
list = list(map(int, input().split()))

for i in range(1, n+1):
    bal.update({i:list[i-1]})
    deque.append(list[i-1])

print(deque[-2])

# while count <= n :
#     print(target)
#     a = bal.get(target)
#     if a < 0 :
#         deque.pop
    
#     target = 
#     count +=1

