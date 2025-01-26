
class Solution:
    def priovIndex(self, nums) -> int:
        leftsum, rightsum = 0, sum(nums)

        for i in range(len(nums)):
            rightsum -= nums[i]

            if rightsum == leftsum:
                return i

            leftsum += nums[i]
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    print(s.priovIndex(nums))