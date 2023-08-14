# https://www.acmicpc.net/problem/1874

# Stack, LIFO

# 리스트 세로로 출력 https://earthteacher.tistory.com/111#gsc.tab=0

import sys

input = sys.stdin.readline

n = int(sys.stdin.readline())
stack = []
answer = []

lastnum = 1

for i in range(1, n + 1):
  num = int(sys.stdin.readline())
  
  while lastnum <= num:
    stack.append(lastnum)
    answer.append("+")
    lastnum+=1
    
  if stack[-1] == num:
    stack.pop()
    answer.append("-")
  else:
    answer.append("NO")
    break

if answer[-1] == "NO":
  print("NO")
else:
  for _ in answer:
    print(_)