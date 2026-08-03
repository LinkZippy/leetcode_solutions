# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        count_max = 0
        test = []
        for num in nums:
            if num - 1 not in set_nums:
                test.append(num)
        for num in test:
            count = 1
            x = num
            while(x+1 in set_nums):
                count += 1
                x += 1
            if count > count_max:
                count_max = count
        return count_max







        
