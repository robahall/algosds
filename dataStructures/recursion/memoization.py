from functools import wraps

def fibonacci(n):
    """
    Simple recursion example to compute fibonacci number

    Recurrence relation: F(n) = F(n-1) + F(n-2)
    Base Case: F(0) = 0 , F(1) = 1

    Example: F(4) = F(3) + F(2) = F(F(2) + F(1)) + F(2) = F(F(1) + F(0) + F(1)) + F(F(1) +F(0)) = 1 + 0 + 1 + 1 + 0

    :param n: (int) specified index for calculating a fibonacci number
    :return: fibonacci number at index n
    """
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def memo_fibonacci(n):
    """
    Add in memoization to cache already computed branches.
    :param n: (int) specified index for calculating a fibonacci number
    :return: fibonacci number at index n
    """
    cache = {}
    def recur_fib(n):
        if n in cache:
            return cache[n]
        if n < 2:
            result = n
        else:
            result = recur_fib(n-1) + recur_fib(n-2)

        cache[n] = result
        return result
    return recur_fib(n)

## How to memoize with decorators:

def cache(func):
    cache = {0: 0, 1: 1}
    def wrapper(idx):
        if idx in cache:
            return cache[idx]
        result = func(idx)
        cache[idx] = result
        return result
    return wrapper

@cache
def dec_fib(n):
    return dec_fib(n-1) + dec_fib(n-2)

## Python decorator internal cache

from functools import lru_cache
@lru_cache(maxsize=None)
def lru_fib(n):
    if n <2:
        return n
    return lru_fib(n-1) + lru_fib(n-2)



if __name__ == "__main__":
    #print(fibonacci(100))
    print(memo_fibonacci(50))
    print(dec_fib(50))
    print(lru_fib(50))