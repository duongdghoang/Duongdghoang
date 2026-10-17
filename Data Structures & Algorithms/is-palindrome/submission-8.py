class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s.lower()[i] == s.lower()[j]:
                i += 1
                j -= 1
            elif s.lower()[i] != s.lower()[j]:
                while i<j and (s[i] == ' ' or not s[i].isalnum()): 
                    i += 1
                while i<j and (s[j] == ' ' or not s[j].isalnum()):
                    j -= 1
                if s.lower()[i] != s.lower()[j]:
                    return False
        return True