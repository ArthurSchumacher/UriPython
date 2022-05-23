from functools import lru_cache

@lru_cache(maxsize=60)
def fibonacci(N):
    if N == 0: return 0
    if N == 1 or N == 2: return 1
    if N > 2: return fibonacci(N - 1) + fibonacci(N - 2)

nTestes = int(input())

for i in range(nTestes):
    nValor = int(input())
    fibonacciLista = []

    for i in range(1, nValor + 1):
        fibonacciLista.append(fibonacci(i))     

    if nValor == 0: print('Fib(0) = 0')
    if nValor >= 1: print('Fib(%d) = %d' % (nValor, fibonacciLista[nValor - 1]))