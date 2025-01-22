from collections import Counter

# method1
class Solution:
    def closeStrings(self, word1, word2) :
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())

#method2
class Solution:
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        word1_dict, word2_dict = {}, {}
        for (s1, s2) in zip(word1, word2):
            if s1 not in word1_dict:
                word1_dict[s1] = 1
            else:
                word1_dict[s1] += 1

            if s2 not in word2_dict:
                word2_dict[s2] = 1
            else:
                word2_dict[s2] += 1


        return sorted(word1_dict.values()) == sorted(word2_dict.values())

if __name__ == '__main__':
    s = Solution()
    word1 = 'aaabbbbccddeeeeefffff'
    word2 = 'aaaaabbcccdddeeeeffff'
    print(s.closeStrings(word1, word2))






