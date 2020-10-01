
def binary_search(arr, key):
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


if __name__ =="__main__":
    arr = [6,13,14,25,33,43,51,53,64,72,84,93,95,96,97]
    print(binary_search(arr, 33))

