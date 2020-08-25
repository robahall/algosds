def pow(x, n):
    """
    Brute force recursion
    where limits are
    -100.0 < x < 100.0
    -2**31 < n < 2**31
    Recursion formula: f(x,n) = x * f(x, n-1) = x * x * f(x, n-2)
    Base Case: f(x,1) = x
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    if n < 0:
        return pow(1/x, -n)
    if n % 2 == 0:
        return pow(x, n//2)*pow(x, n//2)
    if n % 2 == 1:
        return pow(x, n//2)*pow(x, n//2)*x




def pow_memo(x,n):
    """
    Tail recursion
    Recursion formula: f(x,n) = x * f(x, n-1) = x * x * f(x, n-2)
    Base Case: f(x,1) = x
    :param x:
    :param n:
    :return:
    """
    cache = {}
    if n == 0:
        return 1
    elif n < 0:
        x = 1/x
        n = n * -1

    def helper(x, n):
        if n in cache:
            return cache[n]
        if n == 1:
            return x
        if n % 2 == 0:
            return helper(x, n)/2 * helper(x, n/2)
        else:
            return x * helper(x, (n-1)/2) * helper(x, (n-1)/2)

    return helper(x, n)



if __name__ == "__main__":

    print(pow(0.01,10000))