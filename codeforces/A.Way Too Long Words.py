n = int(input())
for i in range(n):
    s = input()
    a = len(s)
    ans = s[0] + str(a-2) + s[-1]
    if a>10:
        print(ans)
    else:
        print(s)
