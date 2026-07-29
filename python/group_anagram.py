# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
  
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for str in strs:
            counts = {}
            for char in str:
                counts[char] = str.count(char)
            signature = tuple(sorted(counts.items()))

            if signature not in groups:
                groups[signature] = []

            groups[signature].append(str)

        return list(groups.values())
        
