class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sv = ''.join(sorted(s))
        tv = ''.join(sorted(t))
        
        if sv == tv:
            return True
        
        return False