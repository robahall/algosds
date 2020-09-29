def maxSubArray(nums):
    n = len(nums)
    curr_sum = max_sum = nums[0]

    for idx in range(1,n):
        curr_sum = max(nums[idx], curr_sum + nums[idx])
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
    nums = [1]
    print(maxSubArray(nums))
    nums = [-1]
    print(maxSubArray(nums))
    nums = [-2147483647]
    print(maxSubArray(nums))