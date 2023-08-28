import sys

N = int(input())
stack = []
for _ in range(N):
    comm = sys.stdin.readline().strip()
    if comm.startswith("push"):
        X = comm.split(" ")[1]
        stack.append(X)
    elif comm.startswith("pop"):
        try:
            print(stack.pop())
        except IndexError:
            print(-1)
    elif comm.startswith("size"):
        print(len(stack))
    elif comm.startswith("empty"):
        print(1) if not stack else print(0)
    elif comm.startswith("top"):
        try:
            print(stack[-1])
        except IndexError:
            print(-1)
