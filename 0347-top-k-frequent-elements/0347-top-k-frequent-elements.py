'''
Hash Map + Sorting → O(n log n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        
        sorted_map = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)

        output = []

        for num, freq in sorted_map[:k]:
            output.append(num) 

        return output           
'''

#Bucket Sort -> O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, value in hashmap.items():
            bucket[value].append(num)

        output = []

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                output.append(num)
            
                if len(output) == k:
                    return output