class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        result_set = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):

                    print(nums[i], nums[j], nums[k], nums[i] + nums[j] + nums[k])
                    if nums[i] + nums[j] + nums[k] == 0:

                        if set([nums[i], nums[j], nums[k]]) not in result_set:
                            result.append([nums[i], nums[j], nums[k]])
                            result_set.append(set([nums[i], nums[j], nums[k]]))
        print(result_set)
        print(result)
        return result


"""
def threeSum(nums):
    # List to store the result
    result = []
    
    # First, sort the array
    nums.sort()
    
    # Loop through the array to fix the first element
    for i in range(len(nums) - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Initialize the two pointers
        left, right = i + 1, len(nums) - 1
        
        # Move the pointers towards each other while they don't cross
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            # If the sum is 0, add the triplet to the result
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicate values for the left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate values for the right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers
                left += 1
                right -= 1
            elif total < 0:
                # If the sum is less than 0, move the left pointer to the right
                left += 1
            else:
                # If the sum is greater than 0, move the right pointer to the left
                right -= 1
    
    # Return the list of triplets that sum to zero
    return result
"""