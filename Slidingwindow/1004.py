import pytest


class Solution():
    def longestOnes(self, nums, k):
        left, maxLength, zeroCount = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)
        return maxLength

@pytest.fixture
def solution():
    return Solution()

def test_longestOnes(solution):
    assert solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
    assert solution.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3) == 10


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
    k = 2
    print(s.longestOnes(nums, k))

