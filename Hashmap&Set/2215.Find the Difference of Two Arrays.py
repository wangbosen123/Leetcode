class solution:
    def findDifference(self, nums1, nums2):
        result = []
        diff1 = list(set(nums1) - set(nums2))
        diff2 = list(set(nums2) - set(nums1))

        result.append(diff1)
        result.append(diff2)

        return result

if __name__ == '__main__':
    s = solution()

    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]

    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]

    print(s.findDifference(nums1, nums2))