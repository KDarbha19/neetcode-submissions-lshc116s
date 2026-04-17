class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse = True)
        for i,j in pair:
            s.append((target - i) / j)
            if len(s) >= 2 and s[-1] <= s[-2]:
                s.pop()
        return len(s) 



            
        