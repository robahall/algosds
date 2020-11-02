def countPrimes(n):
    #Worst case: Iterate through each value and check if prime. O(n^2)
    # Use Sieve of Eratosthenes
    if n < 2:
        return 0
    else:
        arr = [True] * n
        arr[0] = arr[1] = False
        for i in range(2, int(n**(1/2))+1):
            if arr[i]:
                for j in range(i*i, n, i):
                    arr[j] = False
    return sum(arr)





if __name__ == "__main__":
    n = 10
    print(countPrimes(n))