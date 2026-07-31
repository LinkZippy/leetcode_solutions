# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(str(len(word)))
            encoded.append("#")
            encoded.append(word)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        n = 0
        j = len(s)
        while n < j:
            i = n
            while s[i] != "#":
                i += 1
            length = int(s[n:i])
            start = i+1
            end = start + length
            decoded.append(s[start:end])
            n = end
        return decoded


