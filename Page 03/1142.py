N = int(input())
count = 1

for i in range(N):
    print('%d %d %d PUM' % (count, (count + 1), (count + 2)))
    count += 4