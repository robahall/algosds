def merge_sort(nums):
    """
    Top down recursive merge_sort
    :param nums:
    :return:
    """
    # bottom cases: empty or list of a single element
    if len(nums) <= 1:
        return nums

    pivot = int(len(nums) / 2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])
    return merge(left_list, right_list)

def merge(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1

    # append what is remaining in either of the lists
    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])

    return ret

def merge_sort_iter(nums):
    prev = [[n] for n in nums]
    while len(prev) > 1:
        cur = []
        for i in range(0, len(prev), 2):
            cur.append(merge(prev[i], prev[i+1] if i + 1 < len(prev) else []))
        prev = cur
    return prev[0]

def merge_iter(l1, l2):
    merge = []
    idx1 = idx2 = 0
    while idx1 < len(l1) and idx2 < len(l2):
        if l1[idx1] < l2[idx2]:
            merge.append(l1[idx1])
            idx1 +=1
        else:
            merge.append(l2[idx2])
            idx2 +=1
    merge.extend(l1[idx1:])
    merge.extend(l2[idx2:])
    return merge










if __name__ == "__main__":
    arr = [10, 9, 2, 3, 5, 6, 7, 9, 1, 0, 2, 3, 6, 4,7,8]
    print(merge_sort(arr))
    print(merge_sort_iter(arr))