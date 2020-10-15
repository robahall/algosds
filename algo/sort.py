def selection_sort(arr):
    """
    Selection Sort
    Performs sort in O(N**2)

    """
    cursor = 0
    while cursor < len(arr):
        min_idx = cursor
        for idx in range(cursor+1, len(arr)):
            if arr[idx] < arr[min_idx] :
                min_idx = idx
        if min_idx != cursor:
            arr[cursor], arr[min_idx] = arr[min_idx], arr[cursor]
        cursor += 1
    return arr

def insertion_sort(arr):
    """
    Insertion sort - Use when array is partially sorted (runs in O(N).
    Best case = O(N)
    Worst Case = 1/4(O(N**2))
    """
    cursor = 0
    while cursor < len(arr):
        idx = cursor
        cursor += 1
        while idx > 0:
            if arr[idx] < arr[idx-1]:
                arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
            else:
                idx -= 1
    return arr

def shuffle_sort(arr):
    import random

    n = len(arr)
    for idx in range(n):
        rdx = random.randint(0, idx)
        arr[idx], arr[rdx] = arr[rdx], arr[idx]
    return arr









#arr =[40, 83, 78, 24, 19, 90, 30, 35, 12, 69, 66, 75, 72, 77, 23, 70, 76, 74, 60, 36, 37, 55, 2, 87, 97, 29, 3, 67, 33, 21, 26, 54, 39, 86, 48, 95, 1, 18, 91, 32, 42, 5, 49, 44, 51, 63, 47, 94, 53, 15, 17, 6, 57, 25, 92, 46, 52, 71, 73, 61, 34, 68, 31, 20, 9, 43, 7, 88, 81]

def test_selection():
    #arr = [40, 83, 78, 24, 19, 90, 30, 35, 12, 69, 66, 75]
    arr = [40, 83, 78, 24, 19, 90, 30, 35, 12, 69, 66, 75, 72, 77, 23, 70, 76, 74, 60, 36, 37, 55, 2, 87, 97, 29, 3, 67,
           33, 21, 26, 54, 39, 86, 48, 95, 1, 18, 91, 32, 42, 5, 49, 44, 51, 63, 47, 94, 53, 15, 17, 6, 57, 25, 92, 46,
           52, 71, 73, 61, 34, 68, 31, 20, 9, 43, 7, 88, 81]
    selection_sort(arr)

def test_insertion():
    arr = [40, 83, 78, 24, 19, 90, 30, 35, 12, 69, 66, 75]
    insertion_sort(arr)




if __name__ == "__main__":
    #array = [10,1,9,2,8,3,7,4,6,5]
    #print(selection_sort(array))
    #print(insertion_sort(array))
    #print(shuffle_sort(array))
    import timeit
    ssort = timeit.timeit("test_selection()", setup="from __main__ import test_selection")
    print(f"Selection sort run time: {ssort:.2f}s")
    #isort =timeit.timeit("test_insertion()", setup="from __main__ import test_insertion")
    #print(f"Insertion sort run time: {isort:.2f}s")

    # With short array selection sort takes 16s.
    # With long array selection sort takes 233.19s



