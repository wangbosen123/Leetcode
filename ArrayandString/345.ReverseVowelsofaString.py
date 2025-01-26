class Solution:
    def reverseVowels(self, s):
        vowels = ['a', "A", 'e', 'E', 'I', 'i', 'O', 'o', 'U', 'u']

        vowels = [i for i in s if i in "aeiouAEIOU"]
        result = []
        for i in s:
            if i not in "aeiouAEIOU":
                result.append(i)
            else:
                result.append(vowels.pop())

        return "".join(result)





if __name__ == '__main__':
    s = Solution()
    string = 'IceCreAm'
    print(s.reverseVowels(string))