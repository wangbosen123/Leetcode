class Solution:
    def kidswithcandies(self, condies, extraCandies):
        result = [False for _ in range(len(condies))]
        for num in range(len(condies)):
            final_kid_condies = condies[num] + extraCandies

            if final_kid_condies >= max(condies):
                result[num] = True

        return result


if __name__ == '__main__':
    s = Solution()
    condies=[2, 3, 5, 1, 3]
    extraCandies = 3
    print(s.kidswithcandies(condies, extraCandies))