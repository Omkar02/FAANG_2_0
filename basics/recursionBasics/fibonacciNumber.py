def fib(n):
    # base condition
    if n in [0, 1]: return n

    return fib(n - 1) + fib(n - 2)

print(fib(7))