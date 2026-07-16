class Solution:
    def checkSubarraySum(self, nums, k):
        rem_index = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k

            if remainder in rem_index:
                if i - rem_index[remainder] >= 2:
                    return True
            else:
                rem_index[remainder] = i

        return False
