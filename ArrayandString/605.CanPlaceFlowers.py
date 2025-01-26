class Solution:
    def canPlaceFlowers(self, flowerbed, n):

        if len(flowerbed) == 1:
            if flowerbed[0] + n <= 1:
                return True
            else:
                return False

        place = 0
        for num in range(len(flowerbed)):
            if num == 0:
                if flowerbed[num + 1] == 1 or flowerbed[num] == 1:
                    continue
                else:
                    place += 1
                    flowerbed[num] = 1

            elif num == len(flowerbed) - 1:
                if flowerbed[num - 1] == 1 or flowerbed[num] == 1:
                    continue
                else:
                    place += 1
                    flowerbed[num] = 1

            else:
                if flowerbed[num - 1] == 1 or flowerbed[num + 1] == 1 or flowerbed[num] == 1:
                    continue
                else:
                    place += 1
                    flowerbed[num] = 1

        return place >= n



if __name__ == '__main__':
    s = Solution()
    flowerbed=[0, 0, 1, 0, 1]
    n = 1
    print(s.canPlaceFlowers(flowerbed, n))