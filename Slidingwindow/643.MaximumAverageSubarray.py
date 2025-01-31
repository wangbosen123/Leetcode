class Solution:
    def findMaxAverage(self, nums, k):
        init = sum(nums[:k])
        res = sum(nums[:k])

        for i in range(len(nums)-k):
            current = init - nums[i] + nums[k+i]
            init = current

            if current > res:
                res = current

        return res/k




if __name__ == '__main__':
    s = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    # nums = [-1]
    # k = 1
    # nums = [4, 0, 4, 3, 3]
    # k = 5
    print(s.findMaxAverage(nums, k))