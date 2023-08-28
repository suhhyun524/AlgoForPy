T = int(input())
for _ in range(T):
    s = input()
    list = []
    for i in s:
        if i == '(':
            list.append(i)
        else:
            try:
                list.pop()
            except IndexError:
                list.append('X')
                break
    if not list:
        print("YES")
    else:
        print("NO")