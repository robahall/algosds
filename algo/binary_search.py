
def binary_search(arr, key):
    """
    Iterative binary search.
    :param arr:(array) array to search
    :param key:(int) desired value
    :return:
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = int(lo + (hi - lo)/2)
        if key < arr[mid]:
            hi = mid - 1
        elif key > arr[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

def binary_searchr(arr, key):
    """
    Recursive binary search.
    :param arr:(array) array to search
    :param key:(int) desired value
    :return:
    """
    lo, hi = 0, len(arr) - 1
    def recuse(arr, key, lo, hi):
        if lo > hi:
            return -1
        else:
            mid = int(lo+(hi-lo)/2)
            if key == arr[mid]:
                return mid
            elif key < arr[mid]:
                # recuse on the portion left of the middle
                return recuse(arr, key, lo, mid-1)
            else:
                # recuse on the portion right of the middle
                return recuse(arr, key, mid+1, hi)
    return recuse(arr, key, lo, hi)





if __name__ =="__main__":
    arr = [6,13,14,25,33,43,51,53,64,72,84,93,95,96,97]
    print(binary_search(arr, 33))
    print(binary_searchr(arr, 33))

