# https://www.acmicpc.net/problem/10828

# 스택
# 인풋, LILO

import sys
input = sys.stdin.readline
answer = []

n = int(input())

for i in range(0,n):
  line = list(map(str,input().split()))
  if line[0] == 'pop':
    print(-1 if not answer else answer.pop())
  if line[0] == 'push':
    answer.append(int(line[1]))
  if line[0] == 'size':
    print(len(answer))
  if line[0] == 'top':
    print(-1 if not answer else answer[-1])
  if line[0] == 'empty':
    print(1 if not answer else 0)