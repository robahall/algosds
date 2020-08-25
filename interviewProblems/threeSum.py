def threeSumSmaller(nums, target):
    nums.sort()
    triplets = 0
    for left in range(len(nums) - 2):
        triplets += twoSumSmaller(nums, left + 1, target - nums[left])
    return triplets

def twoSumSmaller(nums, start_idx, target):
    triplets = 0
    middle = start_idx
    right = len(nums) - 1
    while middle < right:
        if nums[middle] + nums[right] < target:
            triplets += right - middle
            middle += 1
        else:
            right -= 1
    return triplets

if __name__ == "__main__":
    nums = [3,1,0,-2]
    target = 4
    print(threeSumSmaller(nums, target))
