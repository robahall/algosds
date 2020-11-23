def minMax(arr, idx):

    def maxArr(arr, idx):
        if idx == 0:
            return arr[0]
        else:
            return max(maxArr(arr, idx - 1), arr[idx - 1])

    def minArr(arr, idx):
        if idx == 0:
            return arr[0]
        else:
            return min(minArr(arr, idx - 1), arr[idx - 1])

    return maxArr(arr, idx), minArr(arr, idx)

def min_max(arr, idx):
    """
    More compact version
    """
    if idx == 0:
        return arr[idx], arr[idx]
    else:
        min_arr, max_arr = min_max(arr, idx-1)
        return min(arr[idx-1], min_arr), max(arr[idx-1], max_arr)





if __name__ == "__main__":
    arr = [1,9,2,8,3,7,4,6,5]
    print(minMax(arr, len(arr)))
    print(min_max(arr, len(arr)))
