
def simpleSlidingWindow(arr, k):
    """
    A simple sliding window example
    :param arr: arr
    :param t: subarray size
    :return: max sum
    """
    maxSum = -1 * float("inf")
    currentSum = 0
    for idx in range(len(arr)):
        currentSum += arr[idx]
        if idx >= k-1:
            maxSum = max(maxSum, currentSum)
            currentSum -= arr[idx-(k-1)]
    return maxSum

def dynamicSlidingWindow(arr, targetSum):
    """
    A simple dyanmic sliding window example
    :param arr: arr
    :param targetSum: sum value
    :return: min arr size
    """
    windowSize = float("inf")
    idxStart = 0
    currentSum = 0
    for idxEnd in range(len(arr)):
        currentSum += arr[idxEnd]
        while currentSum >= targetSum:
            windowSize = min(windowSize, idxEnd - idxStart+1)
            currentSum -= arr[idxStart]
            idxStart += 1

    return windowSize

def dynamicSlidingWindowWithHashMap(string, k):
    """
    A simple dyanmic sliding window utilizing a hashmap.
    :param arr: arr
    :param targetSum: sum value
    :return: min arr size
    """
    charHash = {}
    maxSize = 0
    idxStart = 0
    for idxEnd in range(len(string)):
        if string[idxEnd] in charHash.keys():
            charHash[string[idxEnd]] += 1
        else:
            charHash[string[idxEnd]] = 1
        while len(charHash.keys()) > k:
            maxSize = max(maxSize, idxEnd - idxStart)
            charHash[string[idxStart]] -= 1
            if charHash[string[idxStart]] is 0:
                del(charHash[string[idxStart]])
            idxStart += 1


    return maxSize


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    elif len(s) == 0:
        return 0
    else:
        currentLength = 0
        maxLength = 0
        charHash = {}
        idxStart = 0
        for idxEnd in range(len(s)):
            if s[idxEnd] in charHash.keys():
                charHash[s[idxEnd]] +=1
                while charHash[s[idxEnd]] > 1:
                    maxLength = max(maxLength, idxEnd - idxStart)
                    charHash[s[idxStart]] -= 1
                    if charHash[s[idxStart]] is 0:
                        del(charHash[s[idxStart]])
                    idxStart +=1
            else:
                charHash[s[idxEnd]] = 1
                currentLength = len(charHash.keys())
        maxLength = max(currentLength, maxLength)
        return maxLength



if __name__ == "__main__":
    # Find max sum for subarray size of 3
    s = [4,2,2,7,8,1,2,8,1,0]
    k = 3 # max window
    print(simpleSlidingWindow(s, k))

    # Find smallest subarray with given sum
    s = [4, 2, 2, 7, 8, 1, 2, 8, 1, 0]
    target = 8
    print(dynamicSlidingWindow(s, target))

    ## Longest substring length with k distinct characters
    s = "AAAHHIBC"
    distinct = 2
    print(dynamicSlidingWindowWithHashMap(s, distinct))

    s="sjyzaeahyh"
    print(lengthOfLongestSubstring(s))




