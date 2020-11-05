import random

class Solution:


    def __init__(self, nums):
        self.original = nums.copy()
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        for idx in range(len(self.nums)):
            rdx = random.randint(0, idx)
            self.nums[rdx], self.nums[idx] = self.nums[idx], self.nums[rdx]

        return self.nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    print(param_1)
    print(param_2)
