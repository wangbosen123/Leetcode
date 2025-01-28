class Solution:
    def productExceptSelf(self, nums):
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    # nums = [-1, 1, 0, -3, 3]
    print(s.productExceptSelf(nums))