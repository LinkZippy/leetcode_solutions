# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        rank = Counter(nums)
        
        rank_tuple = list(dict(sorted(rank.items(), key = lambda item: item[1], reverse=True)).keys())

        for i in range(k):
            res.append(rank_tuple[i])

        return res



        
