import pytest

class Solution:
    def longestSubarray(self, nums:list[int]):
        left = 0
        res = 0
        zeroCount = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            res = max(res, right-left)

        return res


@pytest.fixture
def solution():
    return Solution


def test_longestSubarray(solution):
    assert solution.longestSubarray(nums=[1, 1, 0, 1]) == 3
    assert solution.longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 0, 1]
    # nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(s.longestSubarray(nums))