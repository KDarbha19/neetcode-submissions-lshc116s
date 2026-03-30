class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        sum = 0
        numb = sorted(nums)
        while r >= l:
            
            sum = numb[l] + numb[r]
            if sum == target: 
                q = nums.index(numb[l])
                p = nums.index(numb[r])
                if q != p:
                    return [min(q,p), max(q,p)]
                else:
                    del nums[q]
                    p = nums.index(numb[r]) + 1
                return [min(q,p), max(q,p)]                
                #return [nums.index(numb[l]), nums.index(numb[r], l + 1)]
                #for i in nums:
                    #if i == numb[r] and nums.index(i) != l:
                        #r = nums.index(i)
                #return [l, r]
            elif sum < target:
                l += 1
            else:
                r -= 1
            
                   


        