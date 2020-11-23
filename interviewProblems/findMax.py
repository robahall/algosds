def maxArr(arr, idx):
    if idx == 0:
        return arr[0]
    else:
        return max(maxArr(arr, idx-1), arr[idx-1])



if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    arr2 = [9,1,8,2,7,3,6,4,5]
    arr3 = [1,2,3,4,5,4,3,2,1]
    print(maxArr(arr, len(arr)))
    print(maxArr(arr2, len(arr2)))
    print(maxArr(arr3, len(arr3)))

