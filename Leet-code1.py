class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums = nums
        self.target = target
        sum_real = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum_val = nums[i] + nums[j]
                if (sum_val == target):
                    index1 = i
                    index2 = j
                    print(f"This is the number {index1}:{nums[i]} & {index2}:{nums[j]}")
                    return [index1, index2]  
                    sum_real = sum_val
                    break
            if sum_real != 0:
                break
                
        # if sum_real != 0:
        #     print(sum_real)
        # else:
        #     print(f"Sum of {self.target} cannot be found in following array!!")

e = Solution()
print(e.twoSum([3,3], 6))
