def containsDuplicate(nums):
    """
    Sort then sweep
    """
    if not nums:
        return False
    nums.sort()  # O(nlogn)
    idx = 0
    while idx + 1 < len(nums):
        if nums[idx] == nums[idx + 1]:
            return True
        else:
            idx += 1
    return False

def containsDuplicateSet(nums):
    """
    Use a set table to store number.
    """
    contains = set()
    for num in nums:
        if num in contains:
            return True
        else:
            contains.add(num)
    return False


if __name__ == "__main__":
    arr = [1,2,3,1]
    print(containsDuplicate(arr))
    print(containsDuplicateSet(arr))
