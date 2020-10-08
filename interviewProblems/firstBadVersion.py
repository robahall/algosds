import bisect

def isBadVersion(i):
    if i >= 5000:
        return True
    else:
        return False



def firstBadVersion(n):
    """
    Binary search algorithm
    Prove its correct by setting n=1
    Use low + (high-low)/2 vs (high+low)/2 due to overflow.

    """
    low = 1
    high = n
    while low < high:
        mid = int(low + (high-low)/2)
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return low



def testBinSearch():
    value = firstBadVersion(100000)



if __name__ == "__main__":
    import timeit
    print(timeit.timeit("testBinSearch()", setup="from __main__ import testBinSearch"))