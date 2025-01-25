
class Solution:
    def maxArea(self, height):
        right, left = 0, len(height)-1
        area = 0
        while right != left:
            area = max(area, min(height[right], height[left]) * (left-right))
            if height[right] < height[left]:
                right += 1
            else:
                left -= 1
        return area


if __name__ == '__main__':
    s = Solution()
    height = [1, 8, 6, 3, 5, 4, 8, 3, 7]
    height = [1, 1]
    print(s.maxArea(height))