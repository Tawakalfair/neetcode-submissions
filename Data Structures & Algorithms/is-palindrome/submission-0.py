class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphnum = ''.join(x.lower() for x in s if x.isalnum())
        reverse_str = alphnum.strip()[::-1]
        return reverse_str == alphnum.strip()
