def twoSum(nums, target):
    checker = {}
    for idx, value in enumerate(nums):
        if target - value in checker:
            return [checker[target-value], idx]
        else:
            checker[value] = idx
    return []

if __name__ == "__main__":
    arr =[0,4,3,0]
    target = 0
    twoSum(arr, target)
