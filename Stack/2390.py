class Solution:
    def removeStars(self, s:str):
        result = []

        for letter in s:
            if letter != "*":
                result.append(letter)
            else:
                result.pop()

        return ''.join(result)



if __name__ == '__main__':
    s = Solution()
    letter = "leet**cod*e"
    # letter = "erase*****"

    print(s.removeStars(letter))

