# Better Solution
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # to check if she eats k bananas can she eat all within h hours
        def k_works(k):
            hours = 0

            for p in piles:
                hours += ceil(p / k)
            
            return hours <= h


        # binary search for the minimum k among the posibilites 1...infinite
        l = 1
        r = max(piles) # koko will only eat the bananas in one pile in one hour so max of the piles


        # it must be left less than right bcoz we say right = k 
        while l < r:
            # out of many posibilites taking the middle one
            k = (l + r) // 2
            
            # if k is yes tht means everything to the right is also yes so shift right to k
            if k_works(k):
                r = k

            # if k is no tht means everything to the left is also no so shift left to k+1    
            else:
                l = k + 1
        
        # both left and right are k so we can return anything
        return r



'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0

        while l <= r:
            k = (l + r) // 2 
            hours = 0

            for p in piles:
                hours += ceil(p / k)
            
            # k is valid
            if hours <= h:
                r = k - 1
            else:
                l = k + 1

        # since loop is l <= r so it runs till l > r
        # when loop l == r at the end, we check one last time, if k is valid r moves r = k - 1
        # but l stays exactly where k was
        return l
'''