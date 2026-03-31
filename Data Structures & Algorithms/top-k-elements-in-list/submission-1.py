class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        dd= dict(sorted(d.items(), key=lambda item: item[1], reverse = True))

        ll = list(dd.keys())
        for i in range(k):
            l.append(ll[i])
        return(l)