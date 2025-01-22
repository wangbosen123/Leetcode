


class solution:
    def movezeroes(self, nums):

        left, right = 0, 0

        for right in range(len(nums)):

            if nums[right] != 0:
                res_right = nums[right]
                res_left = nums[left]

                nums[right] = res_left
                nums[left] = res_right

                # nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    # nums = [-1, 0, 1, 2, -1, -4]
    s = solution()
    print(s.movezeroes(nums=nums))