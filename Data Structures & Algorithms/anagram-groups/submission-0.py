class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = []
        for j in strs:
            new_list.append(''.join(sorted(j)))

        result = {}
        for sorted_word, original_word in zip(new_list, strs):
            if sorted_word not in result:
                result[sorted_word] = []
            result[sorted_word].append(original_word)

        list_result = list(result.values())

        return list_result  

                
                

