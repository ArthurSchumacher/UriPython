greater = 0
position = 0

for i in range(1, 101):
    X = int(input())

    if X > greater:
        greater = X
        position = i

print(greater)
print(position)