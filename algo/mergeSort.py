def merge(arr, low, mid, high):
    # Copy
    aux = list(arr)
    i = low
    j = mid + 1

    # Merge
    for k in range(low, high+1):
        if i > mid:
            arr[k] = aux[j]
            j+=1
        elif j > high:
            arr[k] = aux[i]
            i+=1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j+=1
        else:
            arr[k] = aux[i]
            i+=1
    return arr

def merge_sort(arr, low, high):
    if low < high:
        mid = int((low+high)/2)
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return arr

def test_merge_sort():
    #arr = [40, 83, 78, 24, 19, 90, 30, 35, 12, 69, 66, 75]
    arr = [40, 83, 78, 24, 19, 90, 30, 35, 12, 69, 66, 75, 72, 77, 23, 70, 76, 74, 60, 36, 37, 55, 2, 87, 97, 29, 3, 67, 33, 21, 26, 54, 39, 86, 48, 95, 1, 18, 91, 32, 42, 5, 49, 44, 51, 63, 47, 94, 53, 15, 17, 6, 57, 25, 92, 46, 52, 71, 73, 61, 34, 68, 31, 20, 9, 43, 7, 88, 81]
    merge_sort(arr, 0, len(arr)-1)




if __name__ == "__main__":
    #arr = [9,10,11,12,1,2,3,4]
    # print(merge_sort(arr, 0, 7))
    #arr2 =[40, 83, 78, 24, 19, 90, 30, 35, 12, 69, 66, 75, 72, 77, 23, 70, 76, 74, 60, 36, 37, 55, 2, 87, 97, 29, 3, 67, 33, 21, 26, 54, 39, 86, 48, 95, 1, 18, 91, 32, 42, 5, 49, 44, 51, 63, 47, 94, 53, 15, 17, 6, 57, 25, 92, 46, 52, 71, 73, 61, 34, 68, 31, 20, 9, 43, 7, 88, 81]
    import timeit
    ms_sort = timeit.timeit("test_merge_sort()", setup="from __main__ import test_merge_sort")
    print(f"Merge sort run time: {ms_sort:.2f}s")

    # With short array mergesort takes 18s.
    # With long array mergesort takes 172.3s





