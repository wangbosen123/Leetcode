
class Solution:
    def isSubsequence(self, s, t):
        s_pointer = 0

        for t_pointer in range(len(t)):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
            if s_pointer == len(s):
                return True

        if s_pointer == len(s): return True
        else: return False


if __name__ == '__main__':
    s = 'b'
    t = 'abc'
    solution = Solution()
    print(solution.isSubsequence(s, t))