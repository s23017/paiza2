c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())

result = 1 if c1 / p1 > c2 / p2 else 2
print(result)
