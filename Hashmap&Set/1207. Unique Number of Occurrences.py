class Solution:
    def uniqueOccurences(self, arr):
        freq = {}

        for i in range(len(arr)):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1

        times = set()
        for (key, value) in freq.items():
            if value in times:
                return False
            times.add(value)
        return True

if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    print(s.uniqueOccurences(arr))