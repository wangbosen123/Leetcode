class Solution:
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        print(words)
        return "".join(words)

if __name__ == '__main__':
    s = Solution()
    str = "the sky is blue"
    print(s.reverseWords(str))