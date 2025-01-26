class Solution:
    def gcdOfStrings(self, str1, str2):
        from math import gcd
        if str1 + str2 != str2+str1:
            return ""
        length = gcd(len(str1), len(str2))
        print(length)
        return str1[:length]

if __name__ == '__main__':
    s = Solution()
    str1 = 'ABABAB'
    str2 = 'ABAB'
    print(s.gcdOfStrings(str1, str2))