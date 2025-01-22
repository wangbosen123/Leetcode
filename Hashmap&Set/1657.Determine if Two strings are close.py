class Solution:
    def closeStrings(self, word1, word2) :
        word1_hashmap = {}
        word2_hashmap = {}

        for word in word1:
            if word in word1_hashmap:
                word1_hashmap[word] += 1
            else:
                word1_hashmap[word] = 0

        for word in word2:
            if word in word2_hashmap:
                word2_hashmap[word] += 1
            else:
                word2_hashmap[word] = 0

        word1_type, word1_num = set(), set()
        word2_type, word2_num = set(), set()

        for (key, value) in word1_hashmap.items():
            if key not in word1_type:
                word1_type.add(key)
            if value not in word1_num:
                word1_num.add(value)
        for (key, value) in word2_hashmap.items():
            if key not in word2_type:
                word2_type.add(key)
            if value not in word2_num:
                word2_num.add(value)
        print(word1_type, word1_num, word2_type, word2_num)
        print(word1_type == word2_type)
        return (word1_type == word2_type) and (word1_num == word2_num)

if __name__ == '__main__':
    s = Solution()
    word1 = 'aaabbbbccddeeeeefffff'
    word2 = 'aaaaabbcccdddeeeeffff'
    print(s.closeStrings(word1, word2))






