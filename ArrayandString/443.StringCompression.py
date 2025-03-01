class Solution:
    def compress(self, chars):
        n = len(chars)
        i = 0
        write = 0

        while i < n:
            ch = chars[i]
            consecutive = 0
            while i < n and chars[i] == ch:
                i += 1
                consecutive += 1

            chars[write] = ch
            write += 1

            if consecutive != 1:
                for con in list(str(consecutive)):
                    chars[write] = con
                    write += 1

        return min(write, len(chars))








if __name__ == '__main__':
    s = Solution()
    chars = ["a","a","b","b","c","c","c"]
    chars = ['a']
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(s.compress(chars))