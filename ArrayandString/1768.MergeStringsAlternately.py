class Solution:
    def mergeAlternately(self, word1, word2):
        new_string = ""
        max_length = max(len(word1), len(word2))

        for s in range(max_length):
            if s < len(word1):
                new_string += word1[s]

            if s < len(word2):
                new_string += word2[s]


        return new_string

if __name__ == '__main__':
    s = Solution()
    word1 = 'abcd'
    word2 = 'pq'
    print(s.mergeAlternately(word1, word2))