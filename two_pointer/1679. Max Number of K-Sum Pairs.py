
class Solution:
    def maxOperateions(self, nums, k):
        nums = sorted(nums)
        right, left = 0, len(nums)-1
        result = 0
        print(nums)

        while right < left and len(nums)!= 0:
            print(right, left, nums[right], nums[left])
            if nums[right] + nums[left] == k:
                nums.pop(right)
                nums.pop(left-1)
                left -= 2
                result += 1
            elif nums[right] + nums[left] < k:
                right += 1
            else:
                left -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    # nums = [3, 1, 3, 4, 3]
    # k = 6
    nums = [1, 2, 3, 4]
    k = 5
    nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
    k = 2
    print(s.maxOperateions(nums, k))