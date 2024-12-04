a, b = map(int, input().split())
c, d = map(int, input().split())

print(f"{(a + b) & 0xFFFFFFFF}")
print(f"{(c + d) & 0xFFFFFFFF}")