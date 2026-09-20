class Solution:
    def isValid(self, s: str) -> bool:
        char_data = {")":"(","}":"{","]":"["}
        stack_list = []

        for c in s:
            if c in char_data:
                if stack_list and stack_list[-1] == char_data[c]:
                    stack_list.pop()
                else:
                    return False
            else:
                stack_list.append(c)
        
        if not stack_list:
            return True
        else:
            return False
