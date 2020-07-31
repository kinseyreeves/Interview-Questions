"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
"""
import itertools


def threeSumClosest(nums, target):
    def diff(a,b):
        return abs(a-b)

    best_diff = diff(sum(nums[0:3]),target)

    nums = sorted(nums)
    for i, n in enumerate(nums):

        low = i+1
        high = len(nums)-1

        while low < high:
            summ = n + nums[low] + nums[high]
            if diff(summ,target) < best_diff:
                best_sum = summ
                best_diff = diff(summ,target)
            if(summ < target):
                low+=1
            else:
                high -=1

    return best_sum


# def threeSumClosest(nums, target):
#     def diff(a,b):
#         return abs(a-b)

#     best_diff = diff(sum(nums[0:3]),target)
#     best_sum = sum(nums[0:3])
#     best_vals = nums[0:3]

#     for comb in itertools.combinations(nums, 3):
        
#         if diff(sum(comb),target) < best_diff:
            
#             best_diff = diff(sum(comb),target)
#             best_sum = sum(comb)
#             if(best_diff == 0):
#                 return best_sum
    
#     return best_sum
        


nums = [1,1,1,0]
nums1 = [-1,2,1,-4]

nums2 = [-12,-44,-67,-65,17,17,-80,73,51,46,-48,-43,-31,17,68,25,79,65,-41,18,-68,-7,29,-19,-48,3,-67,73,-57,-90,12,37,-16,-1,-65,47,53,-79,0,-62,-96,-10,-79,-25,38,93,28,6,99,68,-25,-27,-1,-61,70,-50,-54,-93,43,-34,31,98,-56,-70,44,49,-52,13,15,55,63,16,-30,-15,-25,87,75,81,19,17,88,-99,9,-92,-52,75,-16,97,-99,-86,60,-45,-88,99,75,36,-82,-67,-12,-47,37,-44,-45,67,85,-32,57,-11,-35,-51,-25,-38,54,-30,96,-62,-31,53,-79,-19,37,-73,95,-38,-60,72,-8,-24,-46,-61,63,-41,95,37,-79,-1,74,-9,92,97,-34,-69,-43,38,79,64,21,68,64]


print(threeSumClosest(nums2, 189))
