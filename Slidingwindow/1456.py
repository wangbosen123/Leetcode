import pytest

class Solution:
    def maxVowels(self, s:str, k:int):
        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        res = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            res = max(res, count)

        return res

@pytest.fixture
def solution():
    return Solution()

def test_maxVowels(solution):
    assert solution.maxVowels("abciiidef", 3) == 3
    assert solution.maxVowels("aeiou", 2) == 2
    assert solution.maxVowels("leetcode", 3) == 2
    assert solution.maxVowels("weallloveyou", 7) == 4

if __name__ == '__main__':
    s = Solution()
    print(s.maxVowels('weallloveyou', 7))


