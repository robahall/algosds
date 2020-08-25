def kthGrammar(N: int, K: int) -> int:
    """
    Brute Force Recursion
    :param N: Row
    :param K: Index (starting with 1)
    :return: int
    """
    if N == 1 or K ==1:
        return 0
    if kthGrammar(N-1, -(-K//2)) == 0 and K % 2 == 0:
        return 1
    elif kthGrammar(N-1, -(-K//2)) == 0 and K % 2 != 0:
        return 0
    elif kthGrammar(N-1, -(-K//2)) == 1 and K % 2 == 0:
        return 0
    else:
        return 1

def kthGrammarMemo(N: int, K: int) -> int:
    """
    Memoized Recursion
    :param N: Row
    :param K: Index (starting with 1)
    :return: int
    """
    cache = {(1,1): 0}
    def helper(N, K):
        if (N, K) in cache:
            return cache[(N,K)]
        if N == 1 or K == 1:
            result = 0
        elif helper(N - 1, -(-K // 2)) == 0 and K % 2 == 0:
            result = 1
        elif helper(N - 1, -(-K // 2)) == 0 and K % 2 != 0:
            result = 0
        elif helper(N - 1, -(-K // 2)) == 1 and K % 2 == 0:
            result = 0
        else:
            result = 1
        cache[(N, K)] = result
        return result
    return helper(N, K)

def fastestkthGrammer(N: int, K: int) -> int:
    if K > 2 ** (N - 1):
        return None
    if N == 1:
        return 0
    if kthGrammar(N - 1, (K + 1) // 2):
        if K % 2:
            return 1
        else:
            return 0
    else:
        if K % 2:
            return 0
        else:
            return 1




if __name__ == "__main__":
    print(kthGrammarMemo(30,1000))