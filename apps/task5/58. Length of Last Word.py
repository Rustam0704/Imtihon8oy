class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.split(" ")
        i = 1
        while len(ls[-i]) == 0:
            i += 1
        return len(ls[-i])
