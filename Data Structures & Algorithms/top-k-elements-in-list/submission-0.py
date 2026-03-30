from operator import itemgetter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = {}
        arr = []
        ar = []
        for i in nums:
            if i in sol:
                sol[i] += 1
            else:
                sol[i] = 1 
        sor = dict(sorted(sol.items(), key=itemgetter(1),reverse = True))
        arr = list(sor)
        for i in range(k):
            ar.append(arr[i])
        return ar       