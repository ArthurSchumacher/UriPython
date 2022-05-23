a, b = map(int, input().split())

r = a % b

if r < 0:
    r = r + abs(b)

q = (a - r) / b

print(f'{int(q)} {int(r)}')