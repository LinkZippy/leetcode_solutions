# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalpha() or char.isnumeric()).lower()
        length = len(s)
        if length == 1:
            return True
        head = 0
        tail = length - 1
        end = length/2
        while(head < end):
            if s[head] == s[tail]:
                head += 1
                tail -= 1
                continue
            if s[head] != s[tail]:
                return False
        return True


            
        

        
        
