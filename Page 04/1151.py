from functools import lru_cache

@lru_cache(maxsize=46)
def fibonacci(N):
    if N == 0: return 0
    if N == 1 or N == 2: return 1
    if N > 2: return fibonacci(N - 1) + fibonacci(N - 2)

N = int(input())

for i in range(N):
    if i == N - 1: print(fibonacci(i))
    if i != N - 1: print(fibonacci(i), end=' ')