class Solution:
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <=first:
                first = num


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    print(s.increasingTriplet(nums))