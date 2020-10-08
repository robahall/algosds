def selection_sort(arr):
    """
    Selection Sort
    Performs sort in O(N**2)

    """
    cursor = 0
    while cursor < len(arr):
        min_idx = cursor
        for idx in range(cursor+1, len(arr)):
            print(arr[idx], arr[min_idx])
            if arr[idx] < arr[min_idx] :
                min_idx = idx
        if min_idx != cursor:
            arr[cursor], arr[min_idx] = arr[min_idx], arr[cursor]
        cursor += 1
    return arr

if __name__ == "__main__":
    array = [10,1,9,2,8,3,7,4,6,5]
    print(selection_sort(array))

