class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in hash_map:
                hash_map[sorted_word] = [word]
            else:
                hash_map[sorted_word].append(word)
        
        return list(hash_map.values())


'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
'''
