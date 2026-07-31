# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        length = len(nums)
        res = []
        while i < length:
            tmp_res = 1
            if i == 0:
                tmp = nums[1:]
                for num in tmp:
                    tmp_res *= num
                res.append(tmp_res)
                i += 1
            elif i == length - 1:
                tmp = nums[:-1]
                for num in tmp:
                    tmp_res *= num
                res.append(tmp_res)
                i += 1
            else:
                tmp_1 = nums[:i]
                for num1 in tmp_1:
                    tmp_res *= num1
                tmp_2 = nums[i+1:]
                for num2 in tmp_2:
                    tmp_res *= num2
                res.append(tmp_res)
                i += 1
        return res
                
        
