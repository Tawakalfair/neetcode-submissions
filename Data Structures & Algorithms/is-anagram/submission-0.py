class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = ''.join(sorted(s))
        y = ''.join(sorted(t))
        result = False
        if x == y :
            result = True
        
        return result

        